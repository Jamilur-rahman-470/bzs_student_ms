from django.http import request
from django.shortcuts import redirect, render
from decorators.decorators import authenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

@authenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.error(request, 'username or password wrong')
    return render(request, 'account/login.html')


@login_required(login_url='login')
def dashboard(request):
    group = request.user.groups.all()[0]
    if 'admin' == group.name:
        return render(request, 'account/admin-dash.html')
    elif 'student' == group.name:
        return render(request, 'account/student-dash.html')
    else:    
        return render(request, 'account/teacher-dash.html')


def logout_user(request):
    logout(request)
    return redirect('login')