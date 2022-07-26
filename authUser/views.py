import random
import string
from django.shortcuts import render, redirect
from authUser.models import Member
from authUser.forms import signUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from django.conf import settings
import requests
from channelsapp.models import Channel


def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={settings.IP_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def signUp(request):
    form = signUpForm()
    if request.method == 'POST':
        ip, routable = get_client_ip(request)
        can_use_ip = ip is not None and routable
        if can_use_ip:
            geo_info = get_geolocation_for_ip(ip)
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if can_use_ip:
                try:
                    channel = Channel.objects.get(location=geo_info["zip"])
                except:
                    channel = Channel(name="dummy", location=geo_info["zip"])
                    channel.save()
                    channel.name = f"Channel Zip Code - {geo_info['zip']}"
                    channel.save()
            else:
                try:
                    channel = Channel.objects.order_by('?')[0]
                except:
                    channel = Channel(name="Channel Zip Code - 94538")
                    channel.save()
            if channel.member_set.count() < 3:
                user.is_mod = True

            user.channel = channel
            user.save()
            login(request, user)
            return redirect('home')
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

