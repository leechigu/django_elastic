from django.shortcuts import render
from .models import Question



def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.object.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request,'pybo/question_list.html',context)
