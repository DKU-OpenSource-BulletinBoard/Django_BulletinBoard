from django.shortcuts import render
from django.http import HttpResponse

# 게시판 프로그램 메인 화면 구현
def main(request):
    return render(request, 'board/main.html')

# 게시판 화면
def bulletin(request):
    return render(request, 'board/bulletinboard.html')

# 사용자 계정 정보 보기
def userinfo(request):
    return render(request, 'board/userinfo.html')

# Create your views here.
