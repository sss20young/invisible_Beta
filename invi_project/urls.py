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
import invi_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', invi_app.views.about, name="about"),
    path('search/', invi_app.views.search, name="search"),
    path('search/lowprice/', invi_app.views.search_lowprice, name="search_lowprice"),
    path('search/highprice/', invi_app.views.search_highprice, name="search_highprice"),
    path('search/highhits/', invi_app.views.search_highhits, name="search_highhits"),
    path('signup/', invi_app.views.signup, name="signup"),
    path('login/', invi_app.views.login, name="login"),
    path('findpw/', invi_app.views.findpw, name="findpw"),
    path('changepw/', invi_app.views.changepw, name="changepw"),
    path('auth_number/', invi_app.views.auth_number, name="auth_number"),
    path('accounts/', include('allauth.urls')),
    path('', invi_app.views.home, name='main_home'),
    path('save/', invi_app.views.save, name='save'),
    path('mypage/', invi_app.views.mypage, name='mypage'),
]