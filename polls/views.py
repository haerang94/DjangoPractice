from django.shortcuts import render, get_object_or_404
from polls.models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_Date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, qeustion_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
