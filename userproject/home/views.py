from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
# Create your views here.
def home(request):
 
    return render(request,"index.html")
def login(request):
    if request.method=="POST":
        userKoName=request.POST.get('username')
        passKHo=request.POST.get('password')
        user = authenticate(username=userKoName, password=passKHo);
        if user is not None: 
            return redirect('home');
        else:
            return render(request,'login.html')
    return render(request,"login.html")
def logout(request):
    logout(request)
    return redirect('/login');