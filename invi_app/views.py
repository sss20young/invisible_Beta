from django.shortcuts import render
from .models import Lecture, Lecturefeature, User, Userlecture, Feature

q='' # 정렬을 위한 전역 변수 선언

def about(request):
    return render(request, 'about.html')

def search(request):
    qs = Lecture.objects.all()

    global q # 전역 변수로 사용
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs1 = qs.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = qs.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)

    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
    })


def search_lowprice(request):
    qs = Lecture.objects.all()

    if q: # q가 있으면
        qs1 = qs.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = qs.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('lecture_price') # 오름차순 정렬

    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
    })

def search_highprice(request):
    qs = Lecture.objects.all()

    if q: # q가 있으면
        qs1 = qs.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = qs.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('-lecture_price') # 내림차순 정렬

    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
    })

def search_highhits(request):
    qs = Lecture.objects.all()

    if q: # q가 있으면
        qs1 = qs.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = qs.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('lecture_title') # 내림차순 정렬

    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
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