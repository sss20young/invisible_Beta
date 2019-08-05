from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:lecture_id>/', views.detail, name='detail'),
    path('save/', views.save, name='save')
]


