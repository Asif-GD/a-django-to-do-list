from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("register/", views.create_user, name="register_user"),
]
