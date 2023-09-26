from django.db import models
import datetime  

class courts(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class clients_id(models.Model):
    client_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,null=True,default=None)
    def __str__(self):
        return self.client_id

class advocates_roll_number(models.Model):
    roll_number=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.roll_number

class charge_sheet(models.Model):
    accused=models.CharField(max_length=50, primary_key=True)
    charges=models.TextField()
    offense_description=models.TextField()
    other_accused=models.CharField(max_length=50,null=True,default=None)
    evidence=models.TextField(null=True,default=None)
    penalties=models.TextField(null=True,default=None)
    def __str__(self):
        return self.accused
    

class demand_letter(models.Model):
    sender=models.OneToOneField(clients_id,on_delete=models.CASCADE)
    recipient=models.CharField(max_length=50)
    demand=models.TextField()
    deadline=models.DateField()
    documents=models.TextField()
    statement=models.TextField()
    def __str__(self):
        return self.sender
    

class case(models.Model):
    case_number=models.CharField(max_length=50,primary_key=True)
    court=models.OneToOneField(courts,on_delete=models.SET_NULL,default=None,null=True)
    pre_trial_date=models.DateField()
    trial_date=models.DateField()
    decision_date=models.DateField()
    issuance_of_decree=models.TextField(default=None,null=True)
    enforcement=models.TextField(default=None,null=True)
    charge_sheet=models.ForeignKey(charge_sheet,on_delete=models.CASCADE,unique=True,null=True,default=None)
    demand_letter=models.ForeignKey(demand_letter,on_delete=models.CASCADE,unique=True,null=True,default=None)
    def __str__(self):
        return self.case_number

class lawyers(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    roll_number=models.OneToOneField(advocates_roll_number,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=50,null=True,default=None)
    availability=models.BooleanField(default=False)
    private=models.BooleanField(default=False)
    cases=models.ManyToManyField(case,through="cases_instances",null=True)
    def __str__(self):
        return self.roll_number.roll_number
class client(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    client_id=models.OneToOneField(clients_id,on_delete=models.CASCADE)
    cases=models.ManyToManyField(case,through='cases_instances')
    def __str__ (self):
        return self.client_id

class cases_instances(models.Model):
    lawyer=models.ForeignKey(lawyers, on_delete=models.SET_NULL,null=True,default=None)
    cases=models.ForeignKey(case,on_delete=models.SET_NULL,null=True,default=None)
    client=models.ForeignKey(client,on_delete=models.SET_NULL,null=True,default=None)
    status=models.BooleanField(default=False)
    





# Create your models here.
