from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i}",
        "text": f"This is question number {i}"
    } for i in range(200)
]
ANSWERS = [
    {
        "id": i,
        "title": f"Answer {i}",
        "text": f"This is answer number {i}"
    } for i in range(10)
]


def index(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, 5)
    page_obj = paginator.page(page_num)
    return render(request, "index.html", {"questions": page_obj})


def hot(request):
    questions = QUESTIONS[10:]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(questions, 5)
    page_obj = paginator.page(page_num)
    return render(request, "hot.html", {"questions": page_obj})


def question(request, question_id):
    item = QUESTIONS[question_id]
    answers = ANSWERS[5:]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(answers, 3)
    page_obj = paginator.page(page_num)
    return render(request, "question.html", {"question": item, "answers": page_obj})


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def settings(request):
    return render(request, "settings.html")
