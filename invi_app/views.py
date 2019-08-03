from django.shortcuts import render
from .models import Lecture

def about(request):
    return render(request, 'about.html')

def search(request):
    qs = Lecture.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs1 = qs.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = qs.filter(lecture_price__icontains=q) # 회사에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)

    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
    })

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def findpw(request):
    return render(request, 'findpw.html')

def changepw(request):
    return render(request, 'changepw.html')

def auth_number(request):
    return render(request, 'auth_number.html')