from django.shortcuts import render
from invi_app.models import *
# Create your views here.

def selectkeyword(request):
    return render(request, 'selectkeyword.html')

# 선택한 키워드 보여주는 함수
def mytype(request):
    if request.method == 'GET':
        lecture_chars = request.GET.getlist('lecture_char')
        teacher_chars = request.GET.getlist('teacher_char')

        return render(request, 'mytype.html', {'lecture_chars' : lecture_chars, 'teacher_chars': teacher_chars})

''' 키워드 저장 함수 미완성
def save_type(request):
        getfeat = Feature.objects.get(feature_id = int(request.GET['feature_id']))
        getuser = User.objects.get(user_email = str(request.GET['user_email']))

        mytype = Userfeature(feature = getfeat, user_email = getuser)
        mytype.save()

        return render(request, 'mytype.html')
'''