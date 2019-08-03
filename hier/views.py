from django.shortcuts import render, get_object_or_404, redirect
from invi_app.models import Lecture, Lecturefeature, Feature

# Create your views here.
def home(request):

    lecture = Lecture.objects.extra(tables=['lectureFeature'], where=['lectureFeature.lecture_id=lecture.lecture_id AND lectureFeature.feature_id is NULL'])
    
    return render(request, 'home.html', {'lec_list': lecture})

def detail(request, lecture_id):

    lec_detail = get_object_or_404(Lecture, pk=lecture_id)
    lec_id = lec_detail.lecture_id
    print(lec_id)

    lec_feature = Feature.objects.filter(feature_id__lte=11)
    T_feature = Feature.objects.exclude(feature_id__lte=11)

    

    return render(request, 'detail.html', {'lec':lec_detail, 'lec_feature':lec_feature, 'T_feature':T_feature})

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