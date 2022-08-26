from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from utils import get_db_handle
from .forms import RegistrationForm

# setting up local MongoDB connection
db, db_client = get_db_handle("to_do_db_test")
print(db.name)
print(db.list_collection_names())


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
