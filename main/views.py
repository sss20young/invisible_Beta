from django.shortcuts import render
from invi_app.models import Feature, Lecture, Lecturefeature, Teacherfeature, Teacher, Lectureteacher, Lecturecategory, Category
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
subjects = '' # 정렬을 위한 전역 변수 선언
grades = ''
lecture_chars = ''
teacher_chars = ''
price = int()
def main(request):
    return render(request, 'main.html')

def result(request):
    global subjects, grades, lecture_chasr, teacher_chars, price # 전역 변수로 사용
    subjects = request.GET.getlist('subject', '')
    grades = request.GET.getlist('grade', '')
    lecture_chars = request.GET.getlist('lecture_char', '')
    teacher_chars = request.GET.getlist('teacher_char', '')
    price = request.GET.get('price', '')
    
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]
    
    # 강의 폼 필터
    result = Lecture.objects.filter(Q(lecturecategory__category__category2__in=subjects) | Q(lecturecategory__category__category3__in=subjects)).filter(lecturefeature__feature__feature_name__in=lecture_chars).filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars).filter(lecture_price__range=(0,(price+1))).filter(Q(lecturecategory__category__category4__in=grades) | Q(lecturecategory__category__category5__in=grades))

    # 필터 결과 중복 제거
    #result = list(set(result))

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

    lec_feat=zip(result, feature, teacher)
    return render(request, 'best_lecture_result.html', {'subjects':subjects, 'grades':grades, 'lecture_chars':lecture_chars, 'teacher_chars':teacher_chars, 'price':price, 'result':result, 'count':len(result), 'len':len(lec_list), 'lec_feat':lec_feat})

# TODO: 특징이 2개 이상일 때 값을 불러오지 못해서 임시로 예외처리문 발생하게 설정해놓음. (선생님의 경우도 마찬가지)

def result_lowprice(request):
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    global subjects, grades, lecture_chars, teacher_chars, price # 전역 변수로 사용
    # 강의 폼 필터
    price=int(price)
    result = Lecture.objects.filter(Q(lecturecategory__category__category2__in=subjects) | Q(lecturecategory__category__category3__in=subjects)).filter(lecturefeature__feature__feature_name__in=lecture_chars).filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars).filter(lecture_price__range=(0,(price+1))).filter(Q(lecturecategory__category__category4__in=grades) | Q(lecturecategory__category__category5__in=grades))

    # 필터 결과 중복 제거
    #result = list(set(result))

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
    return render(request, 'best_lecture_result.html', {'subjects':subjects, 'grades':grades, 'lecture_chars':lecture_chars, 'teacher_chars':teacher_chars, 'price':price, 'result':result, 'count':len(result), 'len':len(lec_list), 'lec_feat':lec_feat})

def result_highprice(request):

    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    global subjects, grades, lecture_chars, teacher_chars, price # 전역 변수로 사용
    # 강의 폼 필터
    result = Lecture.objects.filter(Q(lecturecategory__category__category2__in=subjects) | Q(lecturecategory__category__category3__in=subjects)).filter(lecturefeature__feature__feature_name__in=lecture_chars).filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars).filter(lecture_price__range=(0,(price+1))).filter(Q(lecturecategory__category__category4__in=grades) | Q(lecturecategory__category__category5__in=grades))

    # 필터 결과 중복 제거
    #result = list(set(result))

    result = result.order_by('-lecture_price') # 오름차순 정렬
    
    for f in lecture_list:
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
    return render(request, 'best_lecture_result.html', {'subjects':subjects, 'grades':grades, 'lecture_chars':lecture_chars, 'teacher_chars':teacher_chars, 'price':price, 'result':result, 'count':len(result), 'len':len(lec_list), 'lec_feat':lec_feat})

def result_highhits(request):
    return render(request, 'best_lecture_result.html')