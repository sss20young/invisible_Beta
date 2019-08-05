# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category1 = models.CharField(max_length=20)
    category2 = models.CharField(max_length=30, blank=True, null=True)
    category3 = models.CharField(max_length=30, blank=True, null=True)
    category4 = models.CharField(max_length=30, blank=True, null=True)
    category5 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    feature_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'feature'


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    lecture_title = models.CharField(max_length=100)
    lecture_price = models.IntegerField()
    lecture_company = models.CharField(max_length=20)
    lecture_day = models.IntegerField(blank=True, null=True)
    lecture_totalnum = models.IntegerField(db_column='lecture_totalNum', blank=True, null=True)  # Field name made lowercase.
    lecture_url = models.CharField(max_length=2083)

    class Meta:
        managed = False
        db_table = 'lecture'


class Lecturebook(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lectureBook'


class Lecturecategory(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lectureCategory'


class Lecturefeature(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    feature = models.ForeignKey(Feature, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectureFeature'


class Lecturepackage(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    package = models.ForeignKey('Package', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lecturePackage'


class Lectureteacher(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lectureTeacher'


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_title = models.CharField(max_length=100)
    package_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_company = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'teacher'
        unique_together = (('teacher_id', 'teacher_company'),)


class Teacherfeature(models.Model):
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)
    feature = models.ForeignKey(Feature, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacherFeature'


class User(models.Model):
    user_email = models.CharField(primary_key=True, max_length=320)
    user_name = models.CharField(max_length=23)
    user_pwd = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user'


class Userfeature(models.Model):
    feature = models.ForeignKey(Feature, models.DO_NOTHING)
    user_email = models.ForeignKey(User, models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'userFeature'


class Userlecture(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    user_email = models.ForeignKey(User, models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'userLecture'