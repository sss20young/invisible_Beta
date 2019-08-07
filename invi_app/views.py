from django.shortcuts import render, redirect
from .models import Lecture, Lecturefeature, Userlecture, Feature, Lectureteacher, User, Teacher
from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

q='' # 정렬을 위한 전역 변수 선언

def about(request):
    return render(request, 'about.html')

def search(request):
    #qs = Lecture.objects.all()
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

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
            lec_company.append(f.lecture_company)

        # 강의 특징 조인 & 강의 선생님 조인
        for i in range(len(lec_list)):
            # 강의 특징 조인
            featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
            try:
                feature.append(featu.get())
            except ObjectDoesNotExist:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)
            except MultipleObjectsReturned:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)

            # 강의 선생님 조인
            teach=Teacher.objects.extra(tables=['lectureTeacher'], where=['lectureTeacher.teacher_id=teacher.teacher_id and lectureTeacher.lecture_id=%s'%lec_list[i]]).values('teacher_name')
            try:
                teacher.append(teach.get())
            except ObjectDoesNotExist:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
            except MultipleObjectsReturned:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
     
    print(lec_list)
    print(feature)
    lec_feat=zip(result, feature, teacher)
    print(lec_feat)
    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
        'len' : len(lec_list),
        'lec_feat' : lec_feat
    })

# TODO: 특징이 2개 이상일 때 값을 불러오지 못해서 임시로 예외처리문 발생하게 설정해놓음. (선생님의 경우도 마찬가지)


def search_lowprice(request):
    #qs = Lecture.objects.all()
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    global q # 전역 변수로 사용
    if q: # q가 있으면
        qs1 = Lecture.objects.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = Lecture.objects.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('lecture_price') # 오름차순 정렬


        for f in result:
            lec_list.append(f.lecture_id)
            lec_company.append(f.lecture_company)

        # 강의 특징 조인 & 강의 선생님 조인
        for i in range(len(lec_list)):
            # 강의 특징 조인
            featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
            try:
                feature.append(featu.get())
            except ObjectDoesNotExist:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)
            except MultipleObjectsReturned:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)

            # 강의 선생님 조인
            teach=Teacher.objects.extra(tables=['lectureTeacher'], where=['lectureTeacher.teacher_id=teacher.teacher_id and lectureTeacher.lecture_id=%s'%lec_list[i]]).values('teacher_name')
            try:
                teacher.append(teach.get())
            except ObjectDoesNotExist:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
            except MultipleObjectsReturned:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
     
    print(lec_list)
    print(feature)
    lec_feat=zip(result, feature, teacher)
    print(lec_feat)
    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
        'len' : len(lec_list),
        'lec_feat' : lec_feat
    })

def search_highprice(request):
    #qs = Lecture.objects.all()
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    global q # 전역 변수로 사용
    if q: # q가 있으면
        qs1 = Lecture.objects.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = Lecture.objects.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('-lecture_price') # 내림차순 정렬


        for f in result:
            lec_list.append(f.lecture_id)
            lec_company.append(f.lecture_company)

        # 강의 특징 조인 & 강의 선생님 조인
        for i in range(len(lec_list)):
            # 강의 특징 조인
            featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
            try:
                feature.append(featu.get())
            except ObjectDoesNotExist:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)
            except MultipleObjectsReturned:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)

            # 강의 선생님 조인
            teach=Teacher.objects.extra(tables=['lectureTeacher'], where=['lectureTeacher.teacher_id=teacher.teacher_id and lectureTeacher.lecture_id=%s'%lec_list[i]]).values('teacher_name')
            try:
                teacher.append(teach.get())
            except ObjectDoesNotExist:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
            except MultipleObjectsReturned:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
     
    print(lec_list)
    print(feature)
    lec_feat=zip(result, feature, teacher)
    print(lec_feat)
    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
        'len' : len(lec_list),
        'lec_feat' : lec_feat
    })

def search_highhits(request):
    #qs = Lecture.objects.all()
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    global q # 전역 변수로 사용
    if q: # q가 있으면
        qs1 = Lecture.objects.filter(lecture_title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        qs2 = Lecture.objects.filter(lecture_price__icontains=q) # 가격에 q가 포함되어 있는 레코드만 필터링
        result = qs1.union(qs2, all=False) # 제목과 본문에 같은 내용이 있으면 중복을 허락하지 않는다.
        # result = qs1.union(qs3, all=False)
        # result = qs2.union(qs3, all=False)
        result = result.order_by('-lecture_title') # 내림차순 정렬


        for f in result:
            lec_list.append(f.lecture_id)
            lec_company.append(f.lecture_company)

        # 강의 특징 조인 & 강의 선생님 조인
        for i in range(len(lec_list)):
            # 강의 특징 조인
            featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
            try:
                feature.append(featu.get())
            except ObjectDoesNotExist:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)
            except MultipleObjectsReturned:
                empty={}
                empty['feature_name']='집계중'
                feature.append(empty)

            # 강의 선생님 조인
            teach=Teacher.objects.extra(tables=['lectureTeacher'], where=['lectureTeacher.teacher_id=teacher.teacher_id and lectureTeacher.lecture_id=%s'%lec_list[i]]).values('teacher_name')
            try:
                teacher.append(teach.get())
            except ObjectDoesNotExist:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
            except MultipleObjectsReturned:
                multiple={}
                multiple['teacher_name']=lec_company[i]
                teacher.append(multiple)
     
    print(lec_list)
    print(feature)
    lec_feat=zip(result, feature, teacher)
    print(lec_feat)
    return render(request, 'search.html', {
        'result' : result,
        'q' : q,
        'count' : len(result),
        'len' : len(lec_list),
        'lec_feat' : lec_feat
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

def mypage(request):
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    user = userLecture.objects.filter(user_email=유저)
    lecture = Lecture.objects.extra(tables=['userLecture'], where=['userLecture.lecture=lecture.lecture_id AND userLecture.user_email = %s'%user])
    
    for lec in lecture:
        lec_list.append(lec.lecture_id)
        lec_company.append(lec.lecture_company)

    # 강의 특징 조인 & 강의 선생님 조인
    for i in range(len(lec_list)):
        # 강의 특징 조인
        featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
        try:
            feature.append(featu.get())
        except ObjectDoesNotExist:
            empty={}
            empty['feature_name']='집계중'
            feature.append(empty)
        except MultipleObjectsReturned:
            empty={}
            empty['feature_name']='집계중'
            feature.append(empty)

        # 강의 선생님 조인
        teach=Teacher.objects.extra(tables=['lectureTeacher'], where=['lectureTeacher.teacher_id=teacher.teacher_id and lectureTeacher.lecture_id=%s'%lec_list[i]]).values('teacher_name')
        try:
            teacher.append(teach.get())
        except ObjectDoesNotExist:
            multiple={}
            multiple['teacher_name']=lec_company[i]
            teacher.append(multiple)
        except MultipleObjectsReturned:
            multiple={}
            multiple['teacher_name']=lec_company[i]
            teacher.append(multiple)
     
    lec_like=zip(lecture, feature, teacher)

    return render(request, 'mypage.html', {'count' : len(user), 'lec_like': lec_like})

def save(request):
    getlec = Lecture.objects.get(lecture_id=int(request.GET['lecture_id']))
    getuser = User.objects.get(user_email=str(request.GET['user_email']))

    # 좋아요한 lecture_id와 user_email 저장
    like = Userlecture(lecture=getlec, user_email=getuser)
    like.save()

    return render(request, 'mypage.html')

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

def hackathon_event(request):
    return render(request, 'hackathon_event.html')
