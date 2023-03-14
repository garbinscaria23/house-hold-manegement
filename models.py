from django.db import models

# Create your models here.

class job(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def _str_(self):
        return self.name

class employee(models.Model):
    f_name=models.CharField(max_length=50,blank=True,null=True)
    l_name=models.CharField(max_length=50,blank=True,null=True)
    DOB=models.DateField(null=True)
    Address=models.TextField(blank=True,null=True)
    gender=models.CharField(max_length=10,null=True)
    pin=models.IntegerField(blank=True,null=True)
    password=models.CharField(max_length=8,blank=True,null=True)
    state=models.CharField(max_length=50,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to='uploads/employee/')
    def _str_(self):
        return self.emp_name

class user(models.Model):
    f_name=models.CharField(max_length=50,blank=True,null=True)
    l_name=models.CharField(max_length=50,blank=True,null=True)
    DOB=models.DateField(null=True)
    gender=models.CharField(max_length=10,null=True)
    Address=models.TextField(blank=True,null=True)
    pin=models.IntegerField(blank=True,null=True)
    password=models.CharField(max_length=8,blank=True,null=True)
    state=models.CharField(max_length=50,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to='uploads/employee/')
    def _str_(self):
        return self.email

class work(models.Model):
    name =models.ForeignKey(job, on_delete=models.CASCADE, blank=True)
    emp_name=models.ForeignKey(employee, on_delete=models.CASCADE, blank=True)
    sheet=models.IntegerField(blank=False,null=True)
    pipe=models.IntegerField(blank=True,null=True)
    other_meterial=models.CharField(max_length=50,blank=True,null=True)
    estimated_quantity=models.IntegerField(default='0',blank=True,null=True)
    purchased_quantity=models.CharField(max_length=50,blank=True,null=True)
    purchased_shop=models.CharField(max_length=50,blank=True,null=True)
    phone_number=models.IntegerField(blank=True,null=True)
    name_of_employees=models.CharField(max_length=50,blank=True,null=True)
    no_of_employees=models.IntegerField(blank=True,null=True)
    workstart=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    #date=models.DateTimeField(auto_now_add=False,auto_now=False)

    def _str_(self):
        return self.emp_name

