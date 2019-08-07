from django.shortcuts import render
from invi_app.models import *
# Create your views here.

def selectkeyword(request):
    return render(request, 'selectkeyword.html')

def mytype(request):
    if request.method == 'GET':
        
        lecture_chars = request.GET.getlist('lecture_char')
        teacher_chars = request.GET.getlist('teacher_char')
        return render(request, 'mytype.html', {'lecture_chars' : lecture_chars, 'teacher_chars': teacher_chars})

'''
def mytype(request):
    if request.method == 'GET':
        lecture_chars = request.GET.getlist('lecture_char')
        teacher_chars = request.GET.getlist('teacher_char')

        return render(request, 'mytype.html', {'lecture_chars' : lecture_chars, 'teacher_chars': teacher_chars})
'''