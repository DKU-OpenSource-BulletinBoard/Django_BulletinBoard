from django.shortcuts import render, redirect
from .forms import BulletinWriteForm
from .models import BulletinBoard
from board.models import User
from board.decorators import login_required
from django.shortcuts import get_object_or_404

def board_view(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session':login_session}
    sp_board = BulletinBoard.objects.filter(board_category = 'Sports')
    pol_board = BulletinBoard.objects.filter(board_category = 'Politics')
    free_board = BulletinBoard.objects.filter(board_category = 'Free')
    context['sp_board'] = sp_board
    context['pol_board'] = pol_board
    context['free_board'] = free_board
    return render(request,'bulletinboard/board_view.html', context)

# 글 쓰기
@login_required
def write(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    if request.method == 'GET':
        w_form = BulletinWriteForm()
        context['forms'] = w_form
        return render(request,'bulletinboard/write_content.html', context)

    elif request.method == 'POST':
        w_form = BulletinWriteForm(request.POST)

        if w_form.is_valid():
            writer_info = User.objects.get(u_id = login_session)
            bulletinboard = BulletinBoard(
                title = w_form.title,
                contents = w_form.contents,
                username = writer_info,
                board_category = w_form.board_category
            )
            bulletinboard.save()
            return redirect('/bulletinboard')
        else:
            context['forms'] = w_form
            if w_form.errors:
                for v in w_form.errors.values():
                    context['error'] = v
                return render(request, 'bulletinboard/write_content.html', context)

def bulletin_detail(request, pk):
    login_session = request.session.get('login_session', '')
    context = {'login_session':login_session}
    board = get_object_or_404(BulletinBoard, id=pk)
    context['board'] = board
    return render(request, 'bulletinboard/detail.html', context)