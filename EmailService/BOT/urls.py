from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:primary_key>/", views.detail, name="detail"),
    path("register/", views.register, name="register"),
    path("user-detail/<int:userID>", views.user_detail, name="user_detail"),
    path("email/", views.send_email, name="send_email"),
    path("login/", views.login, name="login")
]
