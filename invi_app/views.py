from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .forms import SigninForm, SignupForm 

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

def signup(request):#역시 GET/POST 방식을 사용하여 구현한다.
    if request.method == "GET":
        return render(request, 'signup.html', {'f':SignupForm()} )
    
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_email = request.POST['user_email']
            password = request.POST['password']
            password_check=request.POST['password_check']
            if password==password_check:
#cleaned_data는 사용자가 입력한 데이터를 뜻한다.
#즉 사용자가 입력한 password와 password_check가 맞는지 확인하기위해 작성해주었다.

                new_user = User.objects.create_user(user_email,password)
#User.object.create_user는 사용자가 입력한 name, email, password를 가지고 아이디를 만든다.
#바로 .save를 안해주는 이유는 User.object.create를 먼저 해주어야 비밀번호가 암호화되어 저장된다.

                #new_user.save()
                
                
                return render(request, 'main.html')      
            else:
                return render(request, 'signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})#password와 password_check가 다를 것을 대비하여 error를 지정해준다.

        else: #form.is_valid()가 아닐 경우, 즉 유효한 값이 들어오지 않았을 경우는

            return render(request, 'signup.html',{'f':form})

def login(request):#로그인 기능
    if request.method == "GET":
        return render(request, 'login.html', {'f':SigninForm()} )
    
    elif request.method == "POST":
        form = SigninForm(request.POST)
        user_email = request.POST['user_email']
        password = request.POST['password']
        u = User(user_email=user_email, password=password)
        print(u)
#authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
#만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.

        if u: #u에 특정 값이 있다면
            u_email=User.objects.get(pk=user_email)#u 객체로 로그인해라
            request.session['user_email']=user_email
            request.session['password']=password
            return render(request,'main.html',{'u_email':u_email})
        else:
            return render(request, 'login.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    

def findpw(request):
    return render(request, 'findpw.html')

def changepw(request):
    return render(request, 'changepw.html')

def auth_number(request):
    return render(request, 'auth_number.html')

def like_save(request):
    getlec = Lecture.objects.get(lecture_id=int(request.GET['lecture_id']))
    getuser = User.objects.get(user_email=str(request.GET['user_email']))

    # 좋아요한 lecture_id와 user_email 저장
    like = Userlecture(lecture=getlec, user_email=getuser)

    getuser=str(request.session['user_email']) # getuser의 타입 바꿈. Queryset -> str
    lecture = Lecture.objects.extra(tables=['userLecture'], where=['userLecture.lecture_id=lecture.lecture_id AND userLecture.user_email=%s'], params=[getuser])
    if getlec in lecture:
        #like.delete()
        return render(request, 'main.html')
    else:
        like.save()    

    # if Userlecture(lecture=getlec, user_email=getuser) is None:
    #     like.save()
    # else:
    #     like.delete()

    return render(request, 'main.html')

def likedlecture(request):

    # 좋아요한 강의 보여주기
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    getuser=str(request.session['user_email'])
    lecture = Lecture.objects.extra(tables=['userLecture'], where=['userLecture.lecture_id=lecture.lecture_id AND userLecture.user_email=%s'], params=[getuser])

    for lec in lecture:
        lec_list.append(lec.lecture_id)
        lec_company.append(lec.lecture_company)
    
    # 강의 특징 조인 & 강의 선생님 조인
    for i in range(len(lec_list)):
        # 강의 특징 조인
        featu=Feature.objects.extra(tables=['lectureFeature'], where=['lectureFeature.feature_id=feature.feature_id and lectureFeature.lecture_id=%s'%lec_list[i]]).values('feature_name')
        print(featu)
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

    return render(request, 'likedlecture.html', {'count' : len(lecture), 'lec_like': lec_like})

def mytype(request):
    return render(request, 'mytype.html')

def selectkeyword(request):
    return render(request, 'selectkeyword.html')

def logout(request):
    del request.session['user_email']
    del request.session['password']
    return render(request, 'main.html')

def hackathon_event(request):
    return render(request, 'hackathon_event.html')
