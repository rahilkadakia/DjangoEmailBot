from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import EmailMetadata, User
from django.core import serializers
from .forms import RegisterForm, EmailForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print(request.user)
        return HttpResponse("Logged In Response")
    return redirect('/bot/login/')

def detail(request, primary_key):
    try:
        obj = get_object_or_404(EmailMetadata, pk=primary_key)
        serialized_obj = serializers.serialize('json', [obj])
        return HttpResponse(serialized_obj)
    except:
        return HttpResponse("Invalid PK")
    
    
def user_detail(request, userID):
    try:
        obj = get_object_or_404(User, pk=userID)
        serialized_obj = serializers.serialize('json', [obj])
        return HttpResponse(serialized_obj)
    except:
        return HttpResponse("Invalid userID")
    

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Created")
    else:
        form = RegisterForm()
    return render(request, "BOT/register.html", {"form":form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            obj = authenticate(username=username, password=password)

            if obj is not None:
                auth_login(request, obj)
                return redirect('/bot/')
            else:
                messages.error(request, 'Incorrect Credentials')
                print('Incorrect Credentials')
                return redirect('/bot/login/')
    else:
        form = LoginForm()
    return render(request, 'BOT/login.html', {"form": form})


def send_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Email Sent")
    else:
        form = EmailForm()
    return render(request, "BOT/email_body.html", {"form": form})