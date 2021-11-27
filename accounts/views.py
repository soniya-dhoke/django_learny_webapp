from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('most_recent_post')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('most_recent_post')
        else:
            messages.info(request,'Username or Password is Incorrect')
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('most_recent_post')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)