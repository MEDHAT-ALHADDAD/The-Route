from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

def Home(request):
    return render(request,'Home.html')

def rec(request):
    return render(request,'request_page/rec.html')

def results(request):
    return render(request,'request_page/Results.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../home/')
    else:
        form =UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})