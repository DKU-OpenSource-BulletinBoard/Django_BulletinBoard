from django.shortcuts import render

def board_view(request):
    login_confirm = request.session.get('login_session', '')
    context = {'login_session':login_confirm}
    return render(request,'bulletinboard/board_view.html', context)

def write(request):
    login_confirm = request.session.get('login_session', '')
    context = {'login_session':login_confirm}
    return render(request,'bulletinboard/write_content.html', context)

# Create your views here.
