from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from accounts.forms import UserForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/index.html')
        else:
            err = form.error_messages.values()
            return render(request, 'accounts/err.html', {'form': form, 'err':err})
    else:
        form = UserCreationForm()
        form.fields['username'].help_text= None
        form.fields['password1'].help_text= None
        form.fields['password2'].help_text= None
        return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request,'accounts/suc.html')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/signin.html', {'form': form})