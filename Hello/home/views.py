from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,'index.html');    

def about(request):
    return render(request,'about.html');    

def services(request):
    return render(request,'services.html');    

def contact(request):
    if request.method=="POST":
        firstname=request.POST.get('fname');
        lastname=request.POST.get('lname');
        city=request.POST.get('city');
        zip=request.POST.get('zip');
        contactObj =  Contact(firstname=firstname,lastname=lastname,city=city,zip=zip);
        contactObj.save();
        messages.success(request, 'New user has been added')
    return render(request,'contacts.html');    
