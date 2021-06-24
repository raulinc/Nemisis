from django.shortcuts import render, redirect
from django.contrib.admin.forms import AuthenticationForm
from .forms import SignupForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def Userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data= request.POST)
        messages.info(request, form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['name']= request.user.username
                request.session.set_expiry(300)
                return redirect('home')

    form = AuthenticationForm()
    return render(request,'login.html', {'form': form})


def UserRegister(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        messages.info(request,form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Succesfully')
            return redirect('login')
    form = SignupForm()
    return render(request,'register.html',{'form': form})


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UserUpdateForm(instance=request.user)
    lla = User.objects.filter(username='c_user.username')
    return render(request,'home.html',{'form' : form})



def userLogout(request):
    logout(request)
    messages.success(request,'Sucessfully Logout')
    return redirect('login')

def userDelete(request):
    data = request.user
    data.delete()
    messages.success(request,f'User Deleted')
    return redirect('register')