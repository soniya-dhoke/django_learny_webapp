from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is Incorrect')
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request,"Account successfully created!!!")
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)