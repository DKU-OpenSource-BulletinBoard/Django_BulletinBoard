from django.shortcuts import render, redirect
from .forms import BulletinWriteForm
from .models import BulletinBoard
from board.models import User

def board_view(request):
    login_confirm = request.session.get('login_session', '')
    context = {'login_session':login_confirm}
    return render(request,'bulletinboard/board_view.html', context)

# 글 쓰기
def write(request):
    login_confirm = request.session.get('login_session', '')
    context = {'login_session':login_confirm}
    if request.method == 'GET':
        w_form = BulletinWriteForm()
        context['forms'] = w_form
        return render(request,'bulletinboard/write_content.html', context)

    elif request.method == 'POST':
        w_form = BulletinWriteForm(request.POST)
        if w_form.is_valid():
            writer_info = User.objects.get(u_id=login_confirm)
            bulletinboard = BulletinBoard(
                title = w_form.title,
                contents = w_form.contents,
                writer_info = writer_info,
                board_category = w_form.board_category
            )
            bulletinboard.save()
            return redirect ('/bulletinboard')

# Create your views here.
