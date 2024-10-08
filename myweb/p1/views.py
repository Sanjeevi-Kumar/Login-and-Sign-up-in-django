from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login

def first(request):
    return render(request,"first.html")

def login(request):
    if request.method=="POST":
        if request.method == "POST":
            uname = request.POST.get('username')
            upass = request.POST.get('pass1')
            user = authenticate(request, username=uname, password=upass)
            print(uname,upass)
            if user is not None:
                auth_login(request, user)
                print(uname,upass)
                return redirect('first/')
            else:
                return HttpResponse("Username or password is wrong")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        uname = request.POST.get('username')
        upass1 = request.POST.get('pass1')
        upass2 = request.POST.get('pass2')
        if upass1 == upass2:
            my_user = User.objects.create_user(username=uname, password=upass1)
            my_user.save()
            print(name, uname, upass1, upass2)
            return redirect('login/')
        else:
            return HttpResponse("Passwords do not match")
    return render(request,'register.html')