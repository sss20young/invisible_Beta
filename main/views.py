from django.shortcuts import render
from invi_app.models import Feature, Lecture, Lecturefeature, Teacherfeature, Teacher, Lectureteacher, Lecturecategory, Category
from django.db.models import Q

def main(request):
    return render(request, 'main.html')

def result(request):
    subjects = request.GET.getlist('subject')
    grades = request.GET.getlist('grade')
    lecture_chars = request.GET.getlist('lecture_char')
    teacher_chars = request.GET.getlist('teacher_char')
    price = int(request.GET.get('price'))

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
    lecture_list = list(set(lecture_list))
    # lecture_list = Lecture.objects.filter(lecturecategory__category__category1='수능')
    # lecture_list = Lecture.objects.all()
    # lecture_list = Lecture.objects.filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars)
    # lecture_list = Lecture.objects.filter(lectureteacher__teacher__teacherfeature__feature__feature_name__in=teacher_chars)
    # lecture_list = Lecture.objects.filter(lecturecategory__category__category4__in=grades) | Lecture.objects.filter(lecturecategory__category__category5__in=grades)
    # lecture_list = Lecture.objects.filter(lecture_price__range=(0,price))

    return render(request, 'best_lecture_result.html', {'subjects':subjects, 'grades':grades, 'lecture_chars':lecture_chars, 'teacher_chars':teacher_chars, 'price':price, 'lecture_list':lecture_list})