from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.main, name="mainpage"),  # 메인 페이지 연결
    path('bulletin', views.bulletin, name="bulletinboard"),  # 게시판 뷰 연결
    path('info', views.userinfo, name="userinfo"),   # 유저 정보 뷰 연결
    path('register', views.register, name="register"), # 회원 가입 페이지로 연결
    path('login', views.login, name='login'), # 로그인 페이지로 연결
    path('logout', views.logout, name='logout') # 로그아웃
]
