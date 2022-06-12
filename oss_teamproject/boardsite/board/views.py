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
    register_form = RegisterForm()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'board/register.html', context)

    elif request.method == 'POST':
        u_id = request.POST.get('id','')
        u_pw = request.POST.get('pw','')
        u_pw_confirm = request.POST.get('re-pw','')
        u_name = request.POST.get('name', '')
        u_phone = request.POST.get('phone', '')

        if (u_id or u_pw or u_pw_confirm or u_name or u_phone) == '': # 빈 칸이 존재한다면 다시 페이지 로드
            return redirect('/board/register')
        elif u_pw != u_pw_confirm:  # 비밀번호 확인 창과 일치하지 않다면 페이지 다시 로드
            return redirect('/board/register')
        else:
            user = User(
                u_id = u_id,
                u_pw = PasswordHasher().hash(u_pw),
                u_name = u_name,
                u_phone = u_phone
            )
            user.save()
        return redirect('/')

# Create your views here.
