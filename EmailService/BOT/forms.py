from django import forms
from .models import User, EmailMetadata

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class EmailForm(forms.ModelForm):
    subject = forms.CharField(max_length=254, required=False)
    body = forms.CharField(max_length=1000)
    class Meta:
        model = EmailMetadata
        fields = ['userID', 'receiver_email', 'subject', 'body']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))