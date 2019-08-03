# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100, blank=True, null=True)
    book_price = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category1 = models.CharField(max_length=20, blank=True, null=True)
    category2 = models.CharField(max_length=30, blank=True, null=True)
    category3 = models.CharField(max_length=30, blank=True, null=True)
    category4 = models.CharField(max_length=30, blank=True, null=True)
    category5 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feature(models.Model):
    feature_id = models.AutoField(primary_key=True)
    feature_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature'


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    lecture_title = models.CharField(max_length=100, blank=True, null=True)
    lecture_price = models.CharField(max_length=8, blank=True, null=True)
    lecture_company = models.CharField(max_length=20, blank=True, null=True)
    lecture_day = models.IntegerField(blank=True, null=True)
    lecture_totalnum = models.IntegerField(db_column='lecture_totalNum', blank=True, null=True)  # Field name made lowercase.
    lecture_url = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture'


class LectureBook(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lecture_book'


class LectureCategory(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lecture_category'


class LectureFeature(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    feature = models.ForeignKey(Feature, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture_feature'


class LecturePackage(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    package = models.ForeignKey('Package', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lecture_package'


class LectureTeacher(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lecture_teacher'


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_title = models.CharField(max_length=100, blank=True, null=True)
    package_price = models.CharField(max_length=8, blank=True, null=True)
    package_url = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class TeacherFeature(models.Model):
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)
    feature = models.ForeignKey(Feature, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_feature'


class User(models.Model):
    user_pwd = models.CharField(max_length=64)
    user_name = models.CharField(max_length=23, blank=True, null=True)
    user_email = models.CharField(primary_key=True, max_length=320)

    class Meta:
        managed = False
        db_table = 'user'


class UserFeature(models.Model):
    feature = models.ForeignKey(Feature, models.DO_NOTHING)
    user_email = models.ForeignKey(User, models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'user_feature'


class UserLecture(models.Model):
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING)
    user_email = models.ForeignKey(User, models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'user_lecture'
