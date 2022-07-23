import random
import string
from django.shortcuts import render, redirect
from authUser.models import Member
from authUser.forms import signUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = Member.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], password=form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = signUpForm()
    return render(request, "authUser/signUp.html", {'form': form})

def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authUser/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'authUser/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

