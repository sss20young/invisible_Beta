from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), #메인 페이지
    path('result', views.result, name='result'), #메인 폼 결과 페이지
    #path('result/highhits/', views.result_highhits, name="result_highhits"), #메인 폼 결과 조회수 정렬 페이지
    #path('result/hightprice/', views.result_highprice, name="result_highprice"), # 메인 폼 결과 높은가격순 정렬 페이지
    #path('result/lowprice/', views.result_lowprice, name="result_lowprice"), # 메인 폼 결과 낮은가격순 정렬 페이지
]