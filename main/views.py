from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utils import get_db_handle
from django.contrib.auth.models import User

# setting up local MongoDB connection
db, db_client = get_db_handle("to_do_db_test")
print(db.name)
print(db.list_collection_names())

# Create your views here.


def home(request):
    return render(request, "main/home.html", {}, content_type="text/html")
