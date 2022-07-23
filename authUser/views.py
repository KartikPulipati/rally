import random
import string
from django.shortcuts import render, redirect
from authUser.models import Member
from authUser.forms import signUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signUp(request):
    form = signUpForm()

    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.username = form.email
            form.save()
            return redirect('home')
    return render(request, "authUser/signUp.html", {'form': form})

