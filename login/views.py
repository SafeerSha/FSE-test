from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
def log(request):
    return render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')
def dashbord(request):
    d = User.objects.all()
    return render(request,'approval.html',{'data':d})
def uhome(r):
    return render(r,"userhome.html",)

def approved(r):
    return render(r,'approved.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['un']
        email = request.POST['email1']
        password = request.POST['pass']
        myuser = User.objects.create_user(username, email, password)
        myuser.username=username
        myuser.save()
        messages.success(request, 'successfully registered...')
        return redirect(log)


def signin(request):
    if request.method == 'POST':
        uname = request.POST['user']
        pass1 = request.POST['password']
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            if user.is_staff == True:
                login(request, user)
                return redirect(dashbord)
            else:
                request.session['username'] = user.username
                login(request, user)
                return redirect(dashbord)
        else:
            return redirect(signup)