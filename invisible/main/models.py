from django.db import models

# Create your models here.
'''
class LectureForm(models.Model):
    SUBJECT_CHOICES = (
        ('0','토익'),('1','토플'),('2','토스'),('3','오픽'),('4','텝스'),
        ('10','국어'),('11','영어'),('12','수학'),('13','한국사'),('14','제2외국어'),
        ('15','사회'),('16','과학'),('17','국어'),('18','영어'),('19','한국사'),
        ('20','행정법'),('21','사회'),('22','행정학'),('23','과학'),('24','수학'),
        ('25','헌법'),('26','경제학'),('27','회계학'),('28','세법'),('29','사회복지학'),
        ('30','교육학'),('31','공직선거법'),('32','국제법'),('33','관세법'),('34','경영학'),
        ('35','지방자치론'),('36','형소법'),('37','교정학'),('38','국제정치학'),('39','형법'),
        ('40','면접')
    )
    STUDY_CHOICES = (
        ('0','개념꼼꼼'),('1','다양한예시'),('2','공부방향 제시'),('3','시험유형 콕콕'),('4','단기완성'),
        ('5','아이엘츠'),('6','지텔프'),('7','SAT'),('8','제2외국어'),('9','토픽'),
    )
    subject = models.CharField(choices=SUBJECT_CHOICES)
    grade = models.CharField()
    study = models.CharField()
    teacher = models.CharField()
'''