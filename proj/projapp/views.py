from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            unm = a.cleaned_data['username']
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['psw']
            b = regmodel(username=unm, phone=ph, psw=ps)
            b.save()
        return HttpResponse("registration success")
    return render(request, 'registration.html')


def log(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['psw']
            b = regmodel.objects.all()
            for i in b:
                if ph == i.phone and ps == i.psw:
                    return render(request, 'profile_page.html')
                else:
                    return HttpResponse("login failed")
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile_page.html')
