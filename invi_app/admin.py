from django.contrib import admin
from .models import Book, Category, Feature, Lecture, Lecturebook, Lecturecategory, Lecturefeature, Lecturepackage, Lectureteacher, Package, Teacher, Teacherfeature, User, Userfeature, Userlecture

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(Lecture)
admin.site.register(Lecturebook)
admin.site.register(Lecturecategory)
admin.site.register(Lecturefeature)
admin.site.register(Lecturepackage)
admin.site.register(Lectureteacher)
admin.site.register(Package)
admin.site.register(Teacher)
admin.site.register(Teacherfeature)
admin.site.register(User)
admin.site.register(Userfeature)
admin.site.register(Userlecture)
