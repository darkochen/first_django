from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Question


def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in latest_question)
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("This is the detail view of the question : %s" % question_id)

def results(request, question_id):
    return HttpResponse("This is the results of the question: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)