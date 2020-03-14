from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm
from .models import Profile, Follow


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_vaild():
            user = form.save()
            return redirect('accounts:login')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html',{
            'form': form,
        }) 


def login_check(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(username=name, password=pwd)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'accounts/login_fail_info.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form":form})



def logout(request):
    django_logout(request)
    return redirect("/")