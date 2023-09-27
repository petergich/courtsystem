from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import F
from io import BytesIO
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.shortcuts import render, redirect
from django.views import View
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
import os
import mimetypes
from django.core.serializers import serialize
import time
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required
import base64
from django.contrib import messages, auth

def home(request):
    return render(request,"court_system/index.html")
@login_required(login_url="landingpage")
def clientlogin(request):
   clien=client.objects.get(username=request.session.get('username'))
   cases=clien.cases.all()
   print(cases)
   object={"client":clien,"cases":cases}
   return render(request,"court_system/clienthome.html",object)
@login_required(login_url="landingpage")
def lawyerlogin(request):
    return render(request,"court_system/lawyerhome.html")
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if client.objects.filter(username=username).exists:
                auth.login(request, user)
                request.session['username']=username
                return redirect("clienthome")
            if lawyers.objects.filter(username=username).exists:
                auth.login(request, user)
                request.session['username']=username
                return redirect("lawyerhome")
            if not client.objects.filter(username=username).exists and not lawyers.objects.filter(username=username).exists:
                return redirect("landingpage")
        else:
            return redirect("landingpage")
def userlanding(request):
    HttpResponse("loged in successfully")
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
                return render(request,'court_system/index.html',{'error_message':"Lawyer Account Created Successfully"})
            if clients_id.objects.filter(client_id=idNo).exists():
                clienti=client(username=username,email=email,password=clients_password, client_id=clients_id.objects.get(client_id=idNo,))
                user = User.objects.create_user(username=username, password=clients_password, email=email)
                clienti.save()
                user.save()
                return render(request,'court_system/index.html',{'error_message':"Client Account Created successfully"})
# Create your views here.
