from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        cpassword = request.POST['cpwd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,first_name=f_name,last_name=l_name,email=email)
                user.save();
                return redirect('login')
            print("User created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"indexdash.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


