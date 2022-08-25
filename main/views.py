from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utils import get_db_handle

# Create your views here.


def home(request):
    return render(request, "main/home.html", {}, content_type="text/html")
