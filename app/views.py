from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
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
    return page_obj, Paginator(object_list, per_page)


def index(request):
    page_count = 5
    page_obj, paginator = paginate(QUESTIONS, request, page_count)
    return render(request, "index.html", {"questions": page_obj, "pagin": paginator})

def hot(request):
    page_count = 5
    start = 5
    page_obj, paginator = paginate(QUESTIONS[start:], request, page_count)
    return render(request, "hot.html", {"questions": page_obj, "pagin": paginator})


def question(request, question_id):
     item = QUESTIONS[question_id]
     page_count = 2

     page_obj, paginator = paginate(ANSWERS, request, page_count)
     return render(request, "question.html", {"question": item,"questions": page_obj, "answers": page_obj, "pagin": paginator})

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

    page_obj, paginator = paginate(QUESTIONS, request, page_count)
    return render(request, "tag.html", {"questions": page_obj,"pagin": paginator, "tag_name": tag_name})