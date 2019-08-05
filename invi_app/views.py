from django.shortcuts import render, redirect
from .models import Lecture, Lecturefeature, Userlecture, Feature, Lectureteacher, User
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist

q='' # 정렬을 위한 전역 변수 선언

def about(request):
    return render(request, 'about.html')

def search(request):
    #qs = Lecture.objects.all()
    lec_list=[]
    feature=[]

    global q # 전역 변수로 사용
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs1 = Lecture.objects.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = Lecture.objects.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)

        for f in result:
            lec_list.append(f.lecture_id)

        for i in range(len(lec_list)):
            featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
            try:
                feature.append(featu.get())
            except ObjectDoesNotExist:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)
            
     
    print(lec_list)
    print(feature)
    lec_feat=zip(result, feature)
    print(lec_feat)
    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
        'len' : len(lec_list),
        'lec_feat' : lec_feat
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

def main(request):
    return render(request, 'main.html')

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

##############################################################

def mypage(request):
    lecture = Lecture.objects.extra(tables=['userLecture'], where=['userLecture.lecture=lecture.lecture_id AND userLecture.user_email='])
    lecture = Lecture.objects.extra(tables=['lectureFeature'], where=['lectureFeature.lecture_id=lecture.lecture_id AND lectureFeature.feature_id is NULL'])
    lecture = userLecture.objects.filter(user_email=유저)
    return render(request, 'mypage.html', {'lec_list': lecture})
    return render(request, 'mypage.html')

##################################

def save(request):
    getlec = Lecture.objects.get(lecture_id=int(request.GET['lecture_id']))
    getuser = User.objects.get(user_email=str(request.GET['user_email']))

    # 좋아요한 lecture_id와 user_email 저장
    like = Userlecture(lecture=getlec, user_email=getuser)
    like.save()

    return redirect('mypage')
def likedlecture(request):
    return render(request, 'likedlecture.html')

def mytype(request):
    return render(request, 'mytype.html')

def selectkeyword(request):
    return render(request, 'selectkeyword.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'login.html')
