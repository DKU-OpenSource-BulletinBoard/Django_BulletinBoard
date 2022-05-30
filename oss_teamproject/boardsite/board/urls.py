from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name="mainpage"),  # 메인 페이지 연결
    path('bulletin', views.bulletin, name="bulletinboard"),  # 게시판 뷰 연결
    path('info', views.userinfo, name="userinfo"),   # 유저 정보 뷰 연결
]
