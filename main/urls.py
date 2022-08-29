from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.user_tasks, name="user_tasks"),
    path("register/", views.create_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
]
