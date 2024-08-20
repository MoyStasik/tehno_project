import random

from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

from app.forms import LoginForm, RegisterForm, AskForm, AnswerForm, EditProfile
from app.models import Question, question_by_id, answers_by_question_id, Tag, hot_100_question, new_questions, \
    question_by_tag, profile_by_user, tag_by_tag_name, tag_exist, Answer, answers_count, QuestionLike

QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i}",
        "text": f"This is question number {i}"
    } for i in range(20)
]
ANSWERS = [
    {
        "title": f"Answer {i+1}",
        "text": f"This is Answer number {i+1}"
    } for i in range(10)
]
def paginate(object_list, request, per_page = 10):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, per_page )
    page_obj = paginator.page(page_num)
    return page_obj


def index(request):
    #questions = Question.objects.annotate(likes_count=Count('question_likes')).all()
    # questions = Question.objects.all()
    # for q in questions:
    #     q.rate = 0
    #     q.rate = len(QuestionLike.objects.all().filter(question = q.id))
    #     q.save()


    page_count = 5
    quest_pages = new_questions()
    page_obj = paginate(quest_pages, request, page_count)
    context ={
        "page": page_obj,

    }

    return render(request, "index.html", context)

def hot(request):
    page_count = 5
    quest = hot_100_question()
    page_obj = paginate(quest, request, page_count)
    context = {
        "page": page_obj,
    }
    return render(request, "hot.html", context)


@login_required(login_url="/login/", redirect_field_name="continue")
def question(request, question_id):
     item = question_by_id(question_id)
     page_count = 2
     answers = answers_by_question_id(question_id)
     page_obj = paginate(answers, request, page_count)
     if request.method == 'GET':
         answer_form = AnswerForm()
     if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            answ = answer_form.cleaned_data
            profile = profile_by_user(request.user)
            answer = Answer.objects.create(
             status=random.choice(Answer.STATUS_CHOICES),
             user=profile,
             question=question_by_id(question_id),
             content=answ['content'],
             rate=0
            )
            answer.save()
            count = answers_count(question_id)
            count = count // 2 + count % 2
            return HttpResponseRedirect(reverse(("question"), kwargs={'question_id': question_id}) + '?page=' + str(count))
     return render(request, "question.html", context={'question': item, 'answers': page_obj, 'form': answer_form})


@require_http_methods(['GET', 'POST'])
def login(request):
    print(request.GET)
    print(request.POST)
    next = ""

    if request.GET:
        next = request.GET['continue']
        print(next)
    if request.method == 'GET':
        login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(request, **login_form.cleaned_data)
            if user:
                auth_login(request, user)
                if next != "":
                    print(next)
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))

        print('failed to login')
    return render(request, "login.html", context={'form': login_form, 'next': next})

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))

def signup(request):
    if request.method == 'GET':
        user_form = RegisterForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                auth_login(request, user)
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="User saving error!")
    return render(request, "registration.html", {'form': user_form})

@login_required(login_url="/login/", redirect_field_name="continue")
def ask(request):
    if request.method == 'GET':
        question_form = AskForm()
    if request.method == 'POST':
        question_form = AskForm(data=request.POST)
        if question_form.is_valid():
            quest = question_form.cleaned_data
            tags = quest['tag']
            tags = tags.split(", ")
            profile = profile_by_user(request.user)
            question = Question.objects.create(

                user= profile,
                header = quest['header'],
                content = quest['content'],
                rate=0
            )
            for i in tags:
                if tag_exist(i):
                    tag = tag_by_tag_name(i)
                else:
                    tag = Tag.objects.create(
                        tag_name= i
                    )
                    tag.save()
                question.tag.add(tag)
            question.save()
            return redirect(reverse("question", kwargs= {'question_id': question.id}))
    return render(request, "ask.html", context = {'form': question_form})

@login_required(login_url="/login/", redirect_field_name="continue")
@csrf_protect
def settings(request):
    form = EditProfile
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = profile_by_user(request.user)
            prof_image = form.cleaned_data
            profile.avatar = prof_image['image']
            profile.name = prof_image['nickname']
            profile.save()
            return redirect(reverse('settings'))
        else:
            form = EditProfile
    return render(request, "settings.html", {'form': form})

def tag(request, tag_name):
    page_count = 3
    questions = question_by_tag(tag_name)
    page_obj = paginate(questions, request, page_count)
    context = {
        "questions": page_obj,
        "tag_name": tag_name
    }
    return render(request, "tag.html", context)


@require_http_methods(['POST'])
@login_required(login_url="login")
@csrf_protect
def like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    profile = profile_by_user(request.user)
    question_like, question_like_created = QuestionLike.objects.get_or_create(question=question, user=profile)


    if not question_like_created:
        question_like.delete()
        question.rate -= 1
    else:
        question.rate += 1
    question.save()

    return redirect(reverse('index'))


@require_http_methods(['POST'])
@login_required(login_url="login")
@csrf_protect
def like_async(request, question_id):
    print("Я тут")
    question = get_object_or_404(Question, pk=question_id)
    profile = profile_by_user(request.user)
    question_like, question_like_created = QuestionLike.objects.get_or_create(question=question, user=profile)


    if not question_like_created:
        question_like.delete()
        question.rate -= 1
    else:
        question.rate += 1
    question.save()

    return JsonResponse({'likes_count': question.rate})