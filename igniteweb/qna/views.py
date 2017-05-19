from django.shortcuts import render,get_object_or_404
from .models import question_bank , hint
from . import adaptive_learning
import random
# Create your views here.
from django.http import HttpResponse
def index(request):
    # all_question = question_bank.objects.all()
    first_question_id,score,strength_list,weakness_list,medium_list = adaptive_learning.main(99999, 99999)
    return render(request ,'qna/index.html',{'first_question_id':first_question_id})


def details(request , questionid):
    this_question = get_object_or_404(question_bank,pk=questionid)
    this_question.is_correct=2
    next_id = None
    total_question_count = question_bank.objects.count()
    return render(request , "qna/details.html", {'this_question':this_question,'next_id':next_id,'total_question_count':total_question_count})

def check(request, questionid):
    this_question = get_object_or_404(question_bank, pk=questionid)
    total_question_count = question_bank.objects.count()
    users_answer = str(request.GET['Answer'])
    if (this_question.answer == users_answer):
        this_question.is_correct =1
        this_question.save()
        next_id,score,strength_list,weakness_list,medium_list = adaptive_learning.main(int(this_question.id),this_question.is_correct)
        if (next_id==777):
            return render(request, "qna/analysis.html",
                          {"score":score,"strength_list":strength_list,"weakness_list":weakness_list,"medium_list":medium_list})
        else:
            return render(request, "qna/details.html",
                      {'this_question': this_question, 'next_id': next_id,
                       'total_question_count': total_question_count})

    else:
        this_question= get_object_or_404(question_bank, pk=questionid)
        this_question.is_correct = 0
        this_question.save()
        next_id,score,strength_list,weakness_list,medium_list = adaptive_learning.main(int(this_question.id), this_question.is_correct)
        if (next_id==777):
            return render(request, "qna/analysis.html",
                          {"score":score,"strength_list":strength_list,"weakness_list":weakness_list,"medium_list":medium_list})

        elif(next_id==700):
            return render(request,"qna/out_of_question.html",{})

        else:
            return render(request, "qna/details.html",
                      {'this_question': this_question, 'next_id': next_id,
                       'total_question_count': total_question_count})

def analysis(request):
    return render(request, 'qna/analysis.html', {'None': None})
def out_of_question(request):
    return render(request,'qna/out_of_question.html',{})