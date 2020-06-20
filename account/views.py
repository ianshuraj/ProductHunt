from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method=='POST':
            #User wants to sign up
        if request.POST['password']==request.POST['confirmpassword']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html',{'error':'Username already exists'})
            except:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')

        else:
            return render(request,'account/signup.html',{'error':'Password Not Matched'})



    else:
        #user wants to enter info
        return render(request,'account/signup.html')

def login(request):

    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'error':'User not found or Password not matched'})



    else:
        #user wants to enter info
        return render(request,'account/login.html')


    return render(request,'account/login.html')

def logout(request):
    #need to route to home page
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
