from django.shortcuts import render
from django.http import HttpResponse
from .models import clients_id, advocates_roll_number,client,lawyers
from django.http import JsonResponse 
from time import sleep

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
                lawyer.save()
                return render(request,'court_system/index.html',{'error_message':"Lawyer found"})
            if clients_id.objects.filter(client_id=idNo).exists():
                return render(request,'court_system/index.html',{'error_message':"clients found"})
# Create your views here.
