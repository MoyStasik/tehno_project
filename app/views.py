from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Question, question_by_id, answers_by_question_id, Tag, hot_100_question, new_questions, \
    question_by_tag

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
def question(request, question_id):
     item = question_by_id(question_id)
     page_count = 2
     answers = answers_by_question_id(question_id)
     page_obj = paginate(answers, request, page_count)
     return render(request, "question.html", {"question": item, "answers": page_obj})

def login(request):
    return render(request, "login.html")

def logout(request):
    return redirect('/login')

def signup(request):
    return render(request, "registration.html")

def ask(request):
    return render(request, "ask.html")

def settings(request):
    return render(request, "settings.html")

def tag(request, tag_name):
    page_count = 3
    questions = question_by_tag(tag_name)
    page_obj = paginate(questions, request, page_count)
    context = {
        "questions": page_obj,
        "tag_name": tag_name
    }
    return render(request, "tag.html", context)