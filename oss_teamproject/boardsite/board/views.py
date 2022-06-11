from django.shortcuts import render, redirect
from .models import User
from argon2 import PasswordHasher
from django.http import HttpResponse
from .forms import RegisterForm

# 게시판 프로그램 메인 화면 구현
def main(request):
    return render(request, 'board/main.html')

# 게시판 화면
def bulletin(request):
    return render(request, 'board/bulletinboard.html')

# 사용자 계정 정보 보기
def userinfo(request):
    return render(request, 'board/userinfo.html')


# 사용자 정보 등록
def register(request):
    if request.method == 'GET':
        return render(request, 'board/register.html')

    elif request.method == 'POST':
        uid = request.POST.get('id','')
        upw = request.POST.get('pw','')
        pw_confirm = request.POST.get('re-pw','')
        uname = request.POST.get('name', '')
        uphone = request.POST.get('phone', '')

        if (uid or upw or pw_confirm or uname or uphone) == '': # 빈 칸이 존재한다면 다시 페이지 로드
            return redirect('/board/register')
        elif upw != pw_confirm:  # 비밀번호 확인 창과 일치하지 않다면 페이지 다시 로드
            return redirect('/board/register')
        else:
            user = User(
                u_id = uid,
                u_pw = PasswordHasher().hash(upw),
                u_name = uname,
                u_phone = uphone
            )
            user.save()
        return redirect('/')

# Create your views here.
