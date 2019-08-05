"""invi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import main.views
import invi_app.views
import hier.views

urlpatterns=[
    path('invi_app/', include('invi_app.urls')),
    path('hier/', include('hier.urls')),
    path('admin/', admin.site.urls),
    path('search/highhits/', invi_app.views.search_highhits, name="search_highhits"),
    path('save/', invi_app.views.save, name='save'),
    path('mypage/', invi_app.views.mypage, name='mypage'),
    path('', invi_app.views.main, name="main"), #메인 페이지
    path('main/', include('main.urls')),
]