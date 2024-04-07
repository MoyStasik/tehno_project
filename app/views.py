from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i+1}",
        "text": f"This is question number {i+1}"
    } for i in range(20)
]
ANSWERS = [
    {
        "title": f"Answer {i+1}",
        "text": f"This is Answer number {i+1}"
    } for i in range(10)
]

def index(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, 5)
    page_obj = paginator.page(page_num)
    return render(request, "index.html", {"questions": page_obj, "pagin": paginator})

def hot(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:], 5)
    page_obj = paginator.page(page_num)
    return render(request, "hot.html", {"questions": page_obj, "pagin": paginator})


def question(request, question_id):
     item = QUESTIONS[question_id]
     page_num = request.GET.get('page', 1)
     paginator = Paginator(ANSWERS, 2)
     page_obj = paginator.page(page_num)
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
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, 3)
    page_obj = paginator.page(page_num)
    return render(request, "tag.html", {"questions": page_obj,"pagin": paginator, "tag_name": tag_name})