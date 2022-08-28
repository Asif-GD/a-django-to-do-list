from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from database import create_list
from .forms import RegistrationForm, ListCreationForm


# Create your views here.


def home(request):
    return render(request, template_name="main/home.html", context={}, content_type="text/html")


def create_user(request):
    if request.method == "POST":
        new_user_form = RegistrationForm(request.POST)
        if new_user_form.is_valid():
            user = new_user_form.save()
            login(request, user)
            # create a new collection tagged to the user's username to store the lists
            db.create_collection(str(user.username))
            messages.success(request, "Registration Successful. Thank you.")
            return redirect("main:home")
        messages.error(request, "Unsuccessful. Invalid Information.")
    new_user_form = RegistrationForm()
    return render(request, template_name="main/register.html", context={"form": new_user_form},
                  content_type="text/html")


def login_user(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Login successful! You are logged in as {username}")
                return redirect("main:home")
            else:
                messages.error(request, "Login failed, invalid username or password.")
        messages.error(request, "Login failed, invalid username or password.")
    login_form = AuthenticationForm()
    return render(request, template_name="main/login.html", context={"form": login_form}, content_type="text/html")


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:home")


def user_lists(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            create_list_form = ListCreationForm(request.POST)
            if create_list_form.is_valid():
                # tag every list created with the user's username before saving it to the database.
                username = request.user.get_username()
                create_list_form.cleaned_data["username"] = str(username)
                form_data = create_list_form.cleaned_data
                # print(create_list_form.cleaned_data)
                # print(form_data)
                # CRUD Operation from database.py
                create_list(form_data, username)
                messages.success(request, "List creation successful.")
                return redirect("main:user_lists")
            else:
                messages.error(request, "Validation failed, please try again.")
        create_list_form = ListCreationForm()
        return render(request, template_name="main/lists.html", context={"form": create_list_form},
                      content_type="text/html")
    messages.info(request, "Unauthorized access, please login in.")
    return redirect("main:login_user")
