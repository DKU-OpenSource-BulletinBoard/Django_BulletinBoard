from django.shortcuts import render, redirect
from .models import User
from argon2 import PasswordHasher
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

# 게시판 프로그램 메인 화면 구현
def main(request):
    return render(request, 'board/main.html')

# 게시판 화면
def bulletin(request):
    return render(request, 'board/bulletinboard.html')

# 사용자 계정 정보 보기
def userinfo(request):
    return render(request, 'board/userinfo.html')

# 로그인
def login(request):
    loginform = LoginForm()
    context = {'forms': loginform }

    if request.method == 'GET':
        return render(request, 'board/login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'board/login.html', context)

# 사용자 정보 등록
def register(request):
    register_form = RegisterForm()
    context = {'forms': register_form}

    if request.method == 'GET':
        return render(request, 'board/register.html', context)

    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User(
                u_id = register_form.u_id,
                u_pw = register_form.u_pw,
                u_name = register_form.u_name,
                u_phone = register_form.u_phone
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'board/register.html', context)


# Create your views here.
