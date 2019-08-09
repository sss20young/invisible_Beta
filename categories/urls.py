from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('detail/<int:lecture_id>/', views.lecture_detail_page, name='detail'), #lecture_detail
    path('result/', views.select_lecture, name='categoryresult'),
#    path(')

#   path('url')
]

