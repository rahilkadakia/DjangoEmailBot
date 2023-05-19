from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import EmailMetadata, User
from django.core import serializers
from .forms import RegisterForm, EmailForm, LoginForm
from django.contrib import messages

def index(request):
    return HttpResponse("BOT's index page")

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
            try:
                obj = User.objects.get(username=username, password=password)
                return redirect('/bot/')
            except:
                messages.error(request, 'Incorrect Credentials')
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