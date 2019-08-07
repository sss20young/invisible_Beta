from django.shortcuts import render
from invi_app.models import Feature, Lecture, Lecturefeature, Teacherfeature, Teacher, Lectureteacher, Lecturecategory, Category
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def main(request):
    return render(request, 'main.html')

def result(request):
    subjects = request.GET.getlist('subject')
    grades = request.GET.getlist('grade')
    lecture_chars = request.GET.getlist('lecture_char')
    teacher_chars = request.GET.getlist('teacher_char')
    price = int(request.GET.get('price'))
    
    lec_list=[]
    lec_company=[]
    feature=[]
    teacher=[]

    # 강의 폼 필터
    lecture_list = Lecture.objects.filter(Q(lecturecategory__category__category2__in=subjects) | Q(lecturecategory__category__category3__in=subjects)).filter(lecturefeature__feature__feature_name__in=lecture_chars).filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars).filter(lecture_price__range=(0,(price+1))).filter(Q(lecturecategory__category__category4__in=grades) | Q(lecturecategory__category__category5__in=grades))
    '''
    lecture_list = Lecture.objects.filter
    (
        Q(lecturefeature__feature__feature_name__in=lecture_chars) |
        Q(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars) |
        Q(lecture_price__range=(0,price)) |
        (Q(lecturecategory__category__category4__in=grades) | Q(lecturecategory__category__category5__in=grades))
    )
    '''
    # 필터 결과 중복 제거
    lecture_list = list(set(lecture_list))
    
    # lecture_list = Lecture.objects.filter(lecturecategory__category__category1='수능')
    # lecture_list = Lecture.objects.all()
    # lecture_list = Lecture.objects.filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars)
    # lecture_list = Lecture.objects.filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars)
    # lecture_list = Lecture.objects.filter(lecturecategory__category__category4__in=grades) | Lecture.objects.filter(lecturecategory__category__category5__in=grades)
    # lecture_list = Lecture.objects.filter(lecture_price__range=(0,price))

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

        lec_feat=zip(lecture_list, feature, teacher)
    return render(request, 'best_lecture_result.html', {'subjects':subjects, 'grades':grades, 'lecture_chars':lecture_chars, 'teacher_chars':teacher_chars, 'price':price, 'lecture_list':lecture_list, 'count':len(lecture_list), 'len':len(lec_list), 'lec_feat':lec_feat})