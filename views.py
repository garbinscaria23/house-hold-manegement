from django.shortcuts import redirect, render
from . models import *
from django.contrib.auth import login, authenticate
def index(request):
    u=user.objects.all()
    return render(request,'index.html',{'u':u})



def register(request):
    if request.method == "POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        pin=request.POST["pin"]
        password=request.POST["password"]
        state=request.POST["state"]
        phone=request.POST["phone"]
        image=request.FILES["image"]
        email=request.POST["email"]
        u=user.objects.create(f_name=fname,l_name=lname,DOB=dob,gender=gender,Address=address,pin=pin,password=password,state=state,phone=phone,image=image,email=email)
        u.save()
        return redirect("http://127.0.0.1:8088/login")
    else:
        return render(request,'registration.html')

def usrregister(request):
    if request.method == "POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        pin=request.POST["pin"]
        password=request.POST["password"]
        state=request.POST["state"]
        phone=request.POST["phone"]
        image=request.FILES["image"]
        email=request.POST["email"]
        u=employee.objects.create(f_name=fname,l_name=lname,DOB=dob,gender=gender,Address=address,pin=pin,password=password,state=state,phone=phone,image=image,email=email)
        u.save()
        return redirect("http://127.0.0.1:8088/login")
    else:
        return render(request,'user_reg.html')
    

def login(request):
     if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        u = authenticate(request, email=email, password=password)
        if u is not None:
            login(request, u)
        else:
             return render(request,'profile.html')
     else:
          pass
     return render(request,'login.html')

def userhome(request):
    return render(request,'profile.html')


def emphome(request):
    return render(request,'emphome.html')
