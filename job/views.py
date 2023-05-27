from django.shortcuts import redirect, render
from . models import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
from django.urls import reverse
from django.contrib import messages




# def generate_pdf(request):
#     # Get data from the database
#     projects = work.objects.all()

#     # Create a file-like buffer to receive PDF data.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)

#     # Set the font style
#     p.setFont('Helvetica', 12)

#     # Write some text to the PDF
#     p.drawString(100, 750, "Tender for Construction of Roofing Work")
#     p.drawString(100, 730, "---------------------------------------")
#     # Description
#     p.drawString(100, 600, "Description:")
#     p.drawString(100, 580, "The project involves the construction of roofing work for a commercial building in [Insert Location]. The scope of work includes the following:")
#     p.drawString(100, 560, "- Supply and installation of roofing materials")
#     p.drawString(100, 540, "- Design and construction of roofing structure")
#     p.drawString(100, 520, "- Waterproofing and insulation work")
#     p.drawString(100, 500, "- Installation of drainage system")
#     p.drawString(100, 480, "- Safety measures during construction")

#     # Tender Requirements
#     p.drawString(100, 440, "Tender Requirements:")
#     p.drawString(100, 420, "The following documents must be submitted by interested bidders:")
#     p.drawString(100, 400, "- Company profile with relevant experience in roofing work")
#     p.drawString(100, 380, "- Valid trade license and registration documents")
#     p.drawString(100, 360, "- Financial statements for the last three years")
#     p.drawString(100, 340, "- Technical proposal including design and materials to be used")
#     p.drawString(100, 320, "- Work schedule and timeline for completion")
#     p.drawString(100, 300, "- Safety plan and measures during construction")
#     p.drawString(100, 280, "- Price proposal with breakdown of costs")

#     # Instructions
#     p.drawString(100, 240, "Instructions:")
#     p.drawString(100, 220, "Interested bidders should submit their tender documents by [Insert Date and Time] to the following address:")
#     p.drawString(100, 200, "[Insert Address]")
#     p.drawString(100, 180, "Late submissions will not be accepted. Bidders may be required to attend a pre-bid meeting on [Insert Date and Time] at the project site to clarify any questions regarding the scope of work.")
#     p.drawString(100, 160, "The client reserves the right to reject any or all bids and to waive any formalities or irregularities in the bidding process.")

#     # Add a line to the PDF
#     p.line(50, 130, 550, 130)

#     # Iterate over the projects and write them to the PDF
#     p.drawString(100, 100, "List of Projects:")
#     y = 80
#     for project in projects:
#         p.drawString(100, y, "Project Name: {}".format(project.name))
#         p.drawString(100, y-20, "Number of Employees: {}".format(project.no_of_employees))
#         p.drawString(100, y-40, "Sheets: {}".format(project.sheets))
#         p.drawString(100, y-60, "Pipes: {}".format(project.pipe))
#         p.drawString(100, y-80, "Other Materials: {}".format(project.other_meterial))
#         p.drawString(100, y-100, "Total Days to Complete: {}".format(project.total_days_to_complete))
#         p.drawString(100, y-120, "Estimated Cost: {}".format(project.estimated_cost))
#         # Add a line to the PDF
#         p.line(50, y-150, 550, y-150)
        
#         y -= 150

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response







   
    

def index(request):
    # u=user.objects.all()
    u=employee.objects.all()
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
        ul=request.POST["user"]
        print(type(ul))
        print(ul)
        if int(ul) == 1:
            u=user.objects.create(f_name=fname,l_name=lname,DOB=dob,gender=gender,Address=address,pin=pin,password=password,state=state,phone=phone,image=image,email=email)
            u.save()
            messages.info(request,"user Registered Succesfully")
            print("user")
        elif int(ul) == 2:
            u=employee.objects.create(f_name=fname,l_name=lname,DOB=dob,gender=gender,Address=address,pin=pin,password=password,state=state,phone=phone,image=image,email=email)
            u.save()
            messages.info(request,"Employee Registered Succesfully")
            print("employee")
        else:
            pass
        return redirect("http://127.0.0.1:8000/login")
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
        return redirect("http://127.0.0.1:8000/login")
    else:
        return render(request,'user_reg.html')
    

def login(request):
     if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        em=employee.objects.filter(email=email,password=password)
        eu=user.objects.filter(email=email,password=password)
     
        if len(em) == 1:
            request.session['user_id'] = em[0].id
            request.session['user_name'] = em[0].email
            request.session['name']=em[0].f_name+' '+em[0].l_name
            request.session['f_name']=em[0].f_name
            request.session['pin']=em[0].pin
            context = {'uname': request.session['user_name'],'ul':em}
            #send_mail('Login','welcome'+uname,uname)
            return redirect('/emphome')



        elif len(eu) == 1:
            request.session['user_id'] = eu[0].id
            request.session['user_name'] = eu[0].email
            request.session['pin']=eu[0].pin
            context = {'uname': request.session['user_name'],'ua':eu}
            #send_mail('Login','welcome'+uname,uname)
            return redirect('/userhome')
            
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'login.html', context)
     else:
        return render(request,'login.html')




def home(request):
    
    if request.user.is_employee:
        return redirect('emphome')
    else:
        return redirect('userhome')
    
    



def userhome(request):
    pin=request.session['pin']
    u=employee.objects.filter(pin=pin)
    um = user.objects.get(email= request.session['user_name'])
    context = {'uname': um, 'u':u}
    return render(request,'userhome.html',context)
    



def emphome(request):
    pin=request.session['pin']
    u=user.objects.filter(pin=pin)
    id=request.session['user_id']
    email = employee.objects.get(email= request.session['user_name'])
    select=employee.objects.filter(id=id)
    context = {'uname': email,'u':u,'select':select}
    return render(request,'emphome.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
      


def quattion(request):
    username=request.session['name']
    c = user.objects.all()
    if request.method == "POST":
        empname=request.POST.get("empname")
        name=request.POST["name"]
        no_of_employees=request.POST["no_of_employees"]
        sheets=request.POST["sheets"]
        pipe=request.POST["pipe"]
        other_meterial=request.POST["other_meterial"]
        total_days_to_complete=request.POST["total_days_to_complete"]
        estimated_cost=request.POST["estimated_cost"]
        u=work.objects.create(empname=empname,name=name,no_of_employees=no_of_employees,sheets=sheets,pipe=pipe,other_meterial=other_meterial,total_days_to_complete=total_days_to_complete,estimated_cost=estimated_cost)
        u.save()
        return redirect("http://127.0.0.1:8000/quattion")
    else:
        context={
            'username':username,
            'customer': c
        }
        return render(request,'auction.html',context)
    
def mytender(request):
    name=request.session['name']

    u=work.objects.filter(empname=name)
    um = employee.objects.get(email= request.session['user_name'])
    context = {'uname': um, 'u':u}
    return render(request,'mytender.html',context)

def recived_tender(request):
    um = user.objects.get(email= request.session['user_name'])
    us = user.objects.filter(email= request.session['user_name'])
    for i in us:
        f_name = i.f_name
        print(f_name)
    u = work.objects.filter(name=f_name)
    context = {'uname': um, 'u':u}
    return render(request,'recived_tender.html',context)



def update_emp(request,pk):
        print(pk)
        user = employee.objects.get(id=pk)
            
        if request.method == 'POST':
            user.phone = request.POST.get('phone',user.phone)
            user.Address = request.POST.get('address',user.Address)
            user.pin = request.POST.get('pin',user.pin)
            user.password = request.POST.get('password',user.password)
            user.save()
            return redirect('http://127.0.0.1:8000/emphome')
        else:
            return render(request,'empupdate.html', {'user': user})



def update_usr(request,pk):
    print(pk)
    empuser = user.objects.get(id=pk)
            
    if request.method == 'POST':
        empuser.phone = request.POST.get('phone',user.phone)
        empuser.Address = request.POST.get('address',user.Address)
        empuser.pin = request.POST.get('pin',user.pin)
        empuser.password = request.POST.get('password',user.password)
        empuser.save()
        return redirect('http://127.0.0.1:8000/userhome')
    else:

            return render(request,'userupdate.html',{'user': user})



def feed_backs(request):
     if request.method == "POST":
        name_of_emp =request.POST["name_of_emp"]
        feedback=request.POST["feedback"]
        u=feed_back.objects.create(name_of_emp=name_of_emp,feedback=feedback)
        u.save()
        return redirect("http://127.0.0.1:8000/feed_backs")
     else:
        emp=employee.objects.all()
        return render(request,'feedback.html',{'emp':emp})
        # return render(request,'feedback.html')


def logout_view(request):
    logout(request)
    return redirect('/')



def selectemp(request,id):
    emp = employee.objects.get(id=id)
    emp.status = 'You are selected'
    emp.save()
    return redirect('http://127.0.0.1:8000/feed_backs')


