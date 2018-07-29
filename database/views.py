from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Database


from .forms import ContactForm


User = get_user_model()
def home_page(request):
    return render(request, "index.html")

def add(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }

    return render(request, "add.html", context)

def add_database(request):

    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone = request.POST["phone"]
    email = request.POST["email"]

    database = Database(first_name=first_name, last_name=last_name, phone=phone, email=email)

    database.save()


    return render(request, "index.html")

def list_database(request):
    return render(request, "list.html")