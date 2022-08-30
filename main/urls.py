from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lists/", views.user_list, name="user_list"),
    # path("<list_pk>/", views.user_task, name="user_task"),
    path("register/", views.create_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
]
