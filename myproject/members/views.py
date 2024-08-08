from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
      return render(request,"home.html")
def login1(request):
    if request.method == "POST":
        email = request.POST['em']
        pass1 = request.POST['pw']
        try:
            user_db1 = signup1.objects.get(email=email)
        except ObjectDoesNotExist:
            try:
                user_db2 = signup2.objects.get(email=email)
            except ObjectDoesNotExist:
                messages="you dont have an account so please register here.."
                return render(request,'login.html',{'msg':messages})
            else:
                if user_db2.password == pass1:
      
                    request.session['email'] = user_db2.email
                    return render(request, "dashboard2.html")
                else:
                    messages = "password doesn't match"
                    return render(request, 'login.html', {'msg': messages})
        else:
            if user_db1.pwd == pass1:
                request.session['fname'] = user_db1.fname
                request.session['email'] = user_db1.email
                return render(request, "dashboard1.html")
            else:
                messages = "password doesn't match"
                return render(request, 'login.html', {'msg': messages})
    else:
        return render(request, "login.html")



def register(request):
      return render(request,"register.html")

def signup_o(request):
      if request.method=="POST":
            name=request.POST["fname"]
            name1=request.POST["lname"]
            email=request.POST["eml"]
            phone_number=request.POST["phnno"]
            password=request.POST["pswd"]
            confirm_password=request.POST["cpswd"]
            if signup1.objects.filter(email=email).first():
                  #Context={"message": "User already exists"}
                  return render(request,'signup1.html')
            else:
                  user=signup1(fname=name,lname=name1,email=email,ph=phone_number,pwd=password,cpwd=confirm_password)
                  user.save()
                  #context={"message": "Account Successfully created!"}
                  return render(request,'login.html')
      return render(request,'signup1.html')

def signup_u(request):
      if request.method=="POST":
            name=request.POST["uname"]
            email=request.POST["emll"]
            phone_number=request.POST["phno"]
            password=request.POST["pwd"]
            confirm_password=request.POST["cpwd"]
            if signup2.objects.filter(email=email).first():
                  #Context={"message": "User already exists"}
                  return render(request,'signup2.html')
            else:
                  user=signup2(uname=name,email=email,mobile=phone_number,password=password,cpassword=confirm_password)
                  user.save()
                  #context={"message": "Account Successfully created!"}
                  return render(request,'login.html')
      return render(request,'signup2.html')

def org_1(request): 
      if request.method=="POST":
            name=request.POST["name1"]
            Email=request.POST["email1"]
            mobile=request.POST["phone1"]
            e_name=request.POST["event_n"]
            e_type=request.POST["event_t"]
            e_loc=request.POST["event_l"]
            e_theme=request.POST["theme"]
            e_pic=request.POST["img"]
            e_req=request.POST["req"]
            e_budget=request.POST["budget"]
            e_break=request.POST["break"]
            e_service=request.POST.getlist("service",False)
            e_exp=request.POST["exp"]
            e_ref=request.POST["ref"]
            org=organizers(name1=name,email1=Email,mobile1=mobile,ename=e_name,etype=e_type,eloc=e_loc,etheme=e_theme,epic=e_pic,ereq=e_req,ebudget=e_budget,ebreak=e_break,eservice=e_service,experience=e_exp,ref=e_ref)
            org.save()
      return render(request,"organizers.html")

def table(request):
      if request.method=="POST":
          eloc=request.POST.get("eloc")
          etype=request.POST.get("etype")
          organize=organizers.objects.filter(eloc=eloc,etype=etype)
          return render(request,'table.html',{'organizers':organize})
      else:
          organizerss=organizers.objects.all()
          return render(request,'table.html',{'organizers':organizerss})

def person_detail(request):
         if "email" in request.session:
           if request.method=="POST":
                name=request.POST["name"]
                Email=request.POST["email"]
                mobile=request.POST["mob"]
                e_name=request.POST["ename"]
                e_type=request.POST["etype"]
                e_loc=request.POST["eloc"]
                e_theme=request.POST["etheme"]
                e_req=request.POST["ereq"]
                e_budget=request.POST["budget"]
                e_break=request.POST["break"]
                e_service=request.POST.getlist("eservice",False)
                e_exp=request.POST["exp"]
                e_ref=request.POST["ref"]
                id=request.POST.get("id")

                org=organizers.objects.get(id=id)
                org.name1=name
                org.email1=Email
                org.mobile1=mobile
                org.ename=e_name
                org.etype=e_type
                org.eloc=e_loc
                org.etheme=e_theme
                org.ereq=e_req
                org.ebudget=e_budget
                org.ebreak=e_break
                org.eservice=e_service
                org.experience=e_exp
                org.ref=e_ref


                org.save()
                return HttpResponse('data submitted successfully')
               
           else:
                email = request.session["email"]
                organizer = organizers.objects.get(email1=email)
                return render(request, 'person_detail.html', {'organizers': organizer})
         else:
           return HttpResponse("please fill your details in manage_view")

     
    
def event_details(request):
     if request.method=="POST":
          email=request.POST.get("email")
          organizer=organizers.objects.get(email1=email)
          return render(request,"event_details.html",{"organizer":organizer})

      
def o_profile(request):
      if "email" in request.session:
                  email = request.session["email"]
                  organizer = organizers.objects.get(email1=email)
                  return render(request, 'o_profile.html', {'organizers': organizer})
      
      else:
           return HttpResponse("Session expired!")     
      
def u_profile(request):
    if request.session.get("email"):
        email = request.session["email"]
        user = signup2.objects.get(email=email)
        return render(request, 'u_profile.html', {'user': user})
    else:
        return HttpResponse("Session expired!")
    return HttpResponse("Some other response")

     
     

      

def dashboard1(request):
      return render(request,"dashboard1.html")

def dashboard2(request):
      return render(request,"dashboard2.html")

def books(request):
      if "email" in request.session:
            email = request.session["email"]
            user1 = signup2.objects.get(email=email)
            if request.method=="POST":
               date=request.POST.get("date")
               time=request.POST.get("time")
               venue=request.POST.get("venue")
               gcount=request.POST.get("gcount")
               addreq=request.POST.get("addreq")
               new_user=signup2.objects.get(email=email)
               user=book(date=date,time=time,venue=venue,email=new_user,gcount=gcount,addreq=addreq)
               user.save()
               return redirect("book")
      return render(request, 'book.html',{'user1':user1})
   
      
def logout(request):

      return render(request,"home.html")

    
def bookings(request):
     if request.method=="POST":
            email=request.POST.get("email")
            status=request.POST.get("status")
            recipient_list =[email]
            subject= 'approval' 
            message=f"Your request is {status}"
            email_from= settings. EMAIL_HOST_USER
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponse("Notification sent Succesfully")
     else:
            booking_list=book.objects.all()
            return render(request,"bookings.html",{"bookings":booking_list})




def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")


