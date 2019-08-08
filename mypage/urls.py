from django.urls import path
from . import views

urlpatterns = [
    path('selectkeyword', views.selectkeyword, name='selectkeyword'),
    path('mytype', views.mytype, name='mytype'),
]
