from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.http import HttpResponse, JasonResponse
from invi_app.models import Book, Category, Feature, Lecture, Lecturecategory, Lecturefeature, Lecturepackage, Lectureteacher, Package, Teacher, Teacherfeature
# from hitcount.models import HitCount
# from hitcount.views import HitCountMixin
from django.db.models import Q\
#from django.template import *
"""

class Category_default(ListView):
    model = Lecture
#    return render(request, 'category.html')

def lecture_detail(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    return render(request, 'lecture_detail.html')


#redirect url
"""
"""
def category(request):   
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories':categories})
"""
def category(request):
    cate1_list = Category.objects.order_by().values('category1').distinct()
    cate2_list = Category.objects.order_by().values('category2').distinct()
    cate3_list = Category.objects.order_by().values('category3').distinct()
    cate4_list = Category.objects.order_by().values('category4').distinct()
    cate5_list = Category.objects.order_by().values('category5').distinct()
    
    return render(request, 'category.html', {'cate1_list':cate1_list,'cate2_list':cate2_list,'cate3_list':cate3_list,'cate4_list':cate4_list,'cate5_list':cate5_list } )



def select_lecture(request):

#    category1s = request.GET.getlist('cate1')
#    category2s = request.GET.getlist('cate2')
#    category3s = request.GET.getlist('cate3')
#    category4s = request.GET.getlist('cate4')
#    category5s = request.GET.getlist('cate5')

    category1s = request.POST['cate1']
    print(category1s)
    category2s = request.POST['cate2']
    print(category2s)
    category3s = request.POST['cate3']
    print(category3s)
    category4s = request.POST['cate4']
    print(category4s)
    category5s = request.POST['cate5']
    print(category5s)

#        qdict = 

    cate_id = Category.objects.filter(Q(category1=category1s)&Q(category2=category2s)&Q(category3=category3s)&Q(category4=category4s)&Q(category5=category5s))

    lec_list=Lecturecategory.objects.extra(tables=['lectureCategory'], where=['lectureCategory.category_id=%s'%cate_id.get().category_id]).values('lecture_id')

    for lec in lec_list:
        print(lec['lecture_id'])
        lec_name=Lecture.objects.get(pk=lec['lecture_id'])
        print(lec_name.lecture_title)

    print(cate_id.get().category_id)

#    lecture_list = list(set(lecture_list))

    lecture_list = Lecture.objects.filter(Q(lecturecategory__category__category1__in=category1s))

    return render(request, 'category.html', {'lecture_list':lecture_list, 'category1s':category1s, 'category2s':category2s, 'category3s':category3s, 'category4s':category4s, 'category5s':category5s, 'lec_name':lec_name})
"""
    else:
        return render(request, 'category1s','category2s','category3s','category4s','category5')

"""

def lecture_detail_page(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)



 #   lecture_detail = get_
 #   lecture_items = Lecture.objects.raw()
    return render(request, 'lecture_detail.html', {'lecture':lecture_detail})
    #{'lecture_items':lecture_items})

"""
"""
"""
def lecture_direct_url(request):
    lecture_url = 'http://www.ebsi.co.kr/ebs/lms/lmsx/retrieveSbjtDtl.ebs?sbjtId='
    return redirect(request, {'lecture_url': lecture_url})
"""