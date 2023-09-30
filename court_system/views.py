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
from django.http import FileResponse
import os

def download(request):
    # Define the path to your file
    pdf_file_path = 'court_system/constitution/The_Constitution_of_Kenya_2010.pdf'  # Replace with the actual file path

    # Get the file name from the path
    pdf_file_name = os.path.basename(pdf_file_path)

    
    # Open the PDF file for reading
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create an HTTP response with the appropriate content type and filename
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_file_name}"'
        return response

def home(request):
    message=request.GET.get('data')
    return render(request,"court_system/index.html",{"error_message":message})
@login_required(login_url="landingpage")
def clientlogin(request):
   clien=client.objects.get(username=request.session.get('username'))
   cases=clien.cases.all()
   object={"client":clien,"cases":cases}
   return render(request,"court_system/clienthome.html",object)
@login_required(login_url="landingpage")
def searchlawyer(request):
    return render(request,"court_system/searchlawyer.html")
@login_required(login_url="landingpage")
def lawyerlogin(request):
    lawy=lawyers.objects.get(username=request.session.get('username'))
    cases=lawy.cases.all()
    object={"lawyer":lawy,"cases":cases}
    return render(request,"court_system/lawyerhome.html",object)
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                    c=client.objects.get(username=username)
                    print("client")
                    auth.login(request, user)
                    request.session['username']=username
                    return redirect("clienthome")
            except:
                try:
                        c=lawyers.objects.get(username=username)
                        print("Lawyer")
                        auth.login(request, user)
                        request.session['username']=username
                        return redirect("lawyerhome")
                except:
                    if not client.objects.filter(username=username).exists and not lawyers.objects.filter(username=username).exists:
                        message='Invalid Credentials'
                        return redirect('/landingpage?data='+message)
        else:
            message='Invalid Credentials'
            return redirect('/landingpage?data='+message)
def userlanding(request):
    HttpResponse("loged in successfully")
def client_save(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['mail']
        clients_password=request.POST['password']
        idNo=request.POST['idno']
        if client.objects.filter(username=username).exists() or lawyers.objects.filter(username=username).exists():
            message='The Username is already taken'
            return redirect('/landingpage?data='+message)
        if client.objects.filter(client_id=idNo).exists():
            message="A user with the ID already exists"
            return redirect('/landingpage?data='+message)
        if lawyers.objects.filter(roll_number=idNo).exists():
            message="A lawyer with the Roll Number already exists"
            return redirect('/landingpage?data='+message)
        if not clients_id.objects.filter(client_id=idNo).exists() and not advocates_roll_number.objects.filter(roll_number=idNo).exists():
             message="Invalid ID or roll number"
             return redirect('/landingpage?data='+message)
        if not client.objects.filter(username=username).exists() and not lawyers.objects.filter(username=username).exists() and not client.objects.filter(client_id=idNo).exists() and not lawyers.objects.filter(roll_number=idNo).exists():
            if advocates_roll_number.objects.filter(roll_number=idNo).exists():
                lawyer=lawyers(username=username,email=email,password=clients_password,roll_number=advocates_roll_number.objects.get(roll_number=idNo))
                user = User.objects.create_user(username=username, password=clients_password, email=email)
                lawyer.save()
                user.save()
                message="Lawyer account created successfully"
                return redirect('/landingpage?data='+message)
            if clients_id.objects.filter(client_id=idNo).exists():
                clienti=client(username=username,email=email,password=clients_password, client_id=clients_id.objects.get(client_id=idNo,))
                user = User.objects.create_user(username=username, password=clients_password, email=email)
                clienti.save()
                user.save()
                message="Client account created successfully"
                return redirect('/landingpage?data='+message)
# Create your views here.
