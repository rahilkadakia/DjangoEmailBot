from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EmailMetadata, User

admin.site.register(EmailMetadata)
admin.site.register(User)