from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from invi_app.models import Lecture, Lecturefeature, Feature, Lectureteacher, Teacherfeature

##################################

def home(request):

    lecture = Lecture.objects.extra(tables=['lectureFeature'], where=['lectureFeature.lecture_id=lecture.lecture_id AND lectureFeature.feature_id is NULL'])
    
    return render(request, 'home.html', {'lec_list': lecture})

##################################

def detail(request, lecture_id):

    lec_detail = get_object_or_404(Lecture, pk=lecture_id)

    #11까지 강의특징, 강의특징list
    lec_feature = Feature.objects.filter(feature_id__lte=11)
    
    #선생님 수
    teacher = Lectureteacher.objects.extra(tables=['lecture'], where=['lectureTeacher.lecture_id=lecture.lecture_id AND lecture.lecture_id =%s'%lecture_id])
    teacher_num = teacher.count()
    
    #단일강좌면 
    if teacher_num is 1:
        teacher_id = teacher.values('teacher_id').get()['teacher_id']
        teacher_feature = Feature.objects.extra(tables=['teacherFeature'], where=['teacherFeature.feature_id=feature.feature_id AND teacherFeature.teacher_id=%s'%teacher_id]).values('feature_name')
        
        tfl = []
        for tf in teacher_feature:
            
            tfl.append(tf['feature_name'])
    #아니면 
    else :
        tfl = "연합강좌입니다."

    print(tfl)

    return render(request, 'detail.html', {'lec':lec_detail, 'lec_feature':lec_feature, 'teacher_feature':tfl})

##################################

def save(request):
   
    getlec = Lecture.objects.get(lecture_id=int(request.GET['lecID']))
    getfeat = Feature.objects.get(feature_id=int(request.GET['lec_selec_1']))
    
    #특징 저장을 시도
    try:
        #1번특징 저장
        feature1 = Lecturefeature(lecture=getlec, feature=getfeat)
        feature1.save()

        getfeat = Feature.objects.get(feature_id=int(request.GET['lec_selec_2']))
        #2번특징 저장
        feature2 = Lecturefeature(lecture=getlec, feature=getfeat)
        feature2.save()
    #실패할 경우
    except:
        return redirect('/hier/')

    #성공할 경우
    else:
        #NULL 제거
        nullnull = Lecturefeature.objects.filter(lecture=getlec, feature__isnull=True).delete()

    return redirect('/hier/')

##################################

'''
#TODO
# 
# detail에 선생님 특징 출력
# url 앱 내로 옮기기
# restful하게 고치기
# 쿼리문 좀더 효율적으로 고치기
'''