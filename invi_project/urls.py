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
from django.conf.urls import url, include
import invi_app.views
import hier.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', invi_app.views.main, name="main"), #메인 페이지
    path('about/', invi_app.views.about, name="about"), #about(소개) 페이지
    path('search/', invi_app.views.search, name="search"), #검색 페이지
    path('signup/', invi_app.views.signup, name="signup"), #회원가입 페이지
    path('login/', invi_app.views.login, name="login"), #로그인 페이지
    path('findpw/', invi_app.views.findpw, name="findpw"), #비밀번호찾기 페이지
    path('changepw/', invi_app.views.changepw, name="changepw"), #비밀번호 재설정 페이지
    path('auth_number/', invi_app.views.auth_number, name="auth_number"), #인증번호 입력 페이지
    path('logout/', invi_app.views.logout, name='logout'),
    path('likedlecture/',invi_app.views.likedlecture, name='likedlecture'), #좋아요한 강의 페이지
    path('selectkeyword/',invi_app.views.selectkeyword, name='selectkeyword'), #선호하는 키워드 페이지
    path('mytype/',invi_app.views.mytype, name='mytype'), #나의 강의타입 페이지
    path('accounts/', include('allauth.urls')), #소셜로그인
    path('admin/', admin.site.urls),
    url(r'^hier/', include('hier.urls')),
]
