from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../home/')
    else:
        form =UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})