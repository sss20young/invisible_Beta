from django.shortcuts import render
from invi_app.models import *
# Create your views here.

def selectkeyword(request):
    return render(request, 'selectkeyword.html')

# 선택한 키워드 보여주는 함수
def mytype(request):
    getlec=[]
    getteach=[]
    
    if request.GET.getlist('lecture_char') is None:
        if request.method == 'GET':
            lecture_chars = request.GET.getlist('lecture_char')
            teacher_chars = request.GET.getlist('teacher_char')
            getuser_queryset = User.objects.get(user_email=str(request.GET['user_email']))
            getuser_str=str(request.session['user_email'])

            count=0
            
            for lecture in lecture_chars:
                getlec.append(Feature.objects.get(feature_name = lecture))
                # 선택한 feature와 user_email 저장
                mytype = Userfeature(feature = getlec[count], user_email = getuser_queryset)
                
                feature = Feature.objects.extra(tables=['userFeature'], where=['userFeature.feature_id=feature.feature_id AND userFeature.user_email=%s'], params=[getuser_str])
                if getlec in feature:
                    #mytype.delete()
                    return render(request, 'main.html')
                else:
                    mytype.save()
                    count=count+1
                
                count=0

                for teacher in teacher_chars:
                    getteach.append(Feature.objects.get(feature_name = teacher))
                    # 선택한 feature와 user_email 저장
                    mytype = Userfeature(feature = getteach[count], user_email = getuser_queryset)
                
                    feature = Feature.objects.extra(tables=['userFeature'], where=['userFeature.feature_id=feature.feature_id AND userFeature.user_email=%s'], params=[getuser_str])
                    if getlec in feature:
                        #mytype.delete()
                        return render(request, 'main.html')
                    else:
                        mytype.save()
                    count=count+1

        return render(request, 'mytype.html', {'lecture_chars' : lecture_chars, 'teacher_chars': teacher_chars})

    else:
        feat_list=[]
        feature=[]
        teacher=[]

        getuser_str=str(request.session['user_email'])

        features = Feature.objects.extra(tables=['userFeature'], where=['userFeature.feature_id=feature.feature_id AND userFeature.user_email=%s'], params=[getuser_str]).values('feature_name')
        print(features)

        #return render(request, 'mytype.html', {'lecture_chars' : lecture_chars, 'teacher_chars': teacher_chars})
        return render(request, 'mytype.html', {'features' : features})