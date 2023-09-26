from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse 


def home(request):
    return render(request,"court_system/index.html")
def client_login(request):
    return render(request,"court_system/login.html")
def client_signup(request):
    return render(request,"court_system/client_signup.html")
def client_save(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['mail']
        clients_password=request.POST['password']
        idNo=request.POST['idno']
        if client.objects.filter(username=username).exists() or lawyers.objects.filter(username=username).exists():
            return render(request,'court_system/index.html',{'error_message':'THE USERNAME IS ALREADY TAKEN'})
        if client.objects.filter(client_id=idNo).exists():
            return render(request,'court_system/index.html',{'error_message':"A user with the ID already exists"})
        if lawyers.objects.filter(roll_number=idNo).exists():
            return render(request,'court_system/index.html',{'error_message':"A lawyer with the Roll Number already exists"})
        if not clients_id.objects.filter(client_id=idNo).exists() and not advocates_roll_number.objects.filter(roll_number=idNo).exists():
            return render(request,'court_system/index.html',{'error_message':"Invalid ID or roll number"})
        if not client.objects.filter(username=username).exists() and not lawyers.objects.filter(username=username).exists() and not client.objects.filter(client_id=idNo).exists() and not lawyers.objects.filter(roll_number=idNo).exists():
            if advocates_roll_number.objects.filter(roll_number=idNo).exists():
                lawyer=lawyers(username=username,email=email,password=clients_password,roll_number=advocates_roll_number.objects.get(roll_number=idNo))
                user = User.objects.create_user(username=username, password=clients_password, email=email)
                lawyer.save()
                user.save()
                return render(request,'court_system/index.html',{'error_message':"Lawyer found"})
            if clients_id.objects.filter(client_id=idNo).exists():
                return render(request,'court_system/index.html',{'error_message':"clients found"})
# Create your views here.
