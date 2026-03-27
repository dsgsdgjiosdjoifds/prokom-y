from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if request.session.get('next'):
                return redirect(request.session.pop('next'))
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_user')

    if request.GET.get('next'):
        request.session['next'] = request.GET['next']

    return render(request, 'accounts/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')
