from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Registration
from django.http import HttpResponseRedirect
def login_register(request):
    nt=""
    if request.GET:
        nt=request.GET.get("next")
    x=Registration.objects.all()
    list_username=[]
    list_email=[]
    login_cred={}
    for i in x:
        list_username.append(i.username)
        list_email.append(i.email)
        login_cred[i.username]=i.password
    print(list_username)
    print(list_email)
    if request.method=="POST":
        Name=request.POST.get("Name","Default")
        Email=request.POST.get("Email","Default")
        username=request.POST.get("username","Default")
        password=request.POST.get("password","Default")
        repassword=request.POST.get("repassword","Default")
        dob=request.POST.get("dob","Default")
        gender=request.POST.get("gender","Default")
        username_login=request.POST.get("username_login","Default")
        password_login=request.POST.get("password_login","Default")
        if Name!="Default":
            if Email in list_email:
                return render(request,"snl.html",{"message":"Email Already Exist","next":nt})
            elif username in list_username:
                return render(request,"snl.html",{"message":"Username Already Exist","next":nt})
            elif password!=repassword:
                return render(request,"snl.html",{"message":"Password is not matching","next":nt})
            else:
                Registration(name=Name,email=Email,username=username,password=password,date_of_birth=dob,gender=gender).save()
                u=User.objects.create_user(username,Email,password)
                u.name=Name
                u.save()
        else:
            if username_login in list_username:
                if password_login==login_cred[username_login]:
                    user=authenticate(request,username=username_login,password=password_login)
                    request.session.set_expiry(300)
                    login(request,user)
                    if nt=="":
                        return HttpResponseRedirect("/Dashboard")
                    else:
                        return HttpResponseRedirect(nt)
                else:
                    return render(request,"snl.html",{"message":"Password Doesnt Match","next":nt})
            else:
                return render(request,"snl.html",{"message":"Username Doesnt exist","next":nt})
    return render(request,"snl.html",{"message":"","next":nt})
@login_required(login_url="/")
def logot(request):
    logout(request)
    return HttpResponseRedirect("/")
@login_required(login_url="/")
def Dashboard(request):
    return HttpResponse("Hello")