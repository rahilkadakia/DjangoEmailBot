from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import EmailMetadata, User
from django.core import serializers
from .forms import RegisterForm

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