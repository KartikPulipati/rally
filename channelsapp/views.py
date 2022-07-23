from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ipware import get_client_ip
import requests
from .models import Channel
from django.conf import settings

def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/98.207.57.21?access_key={settings.IP_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

class ChannelView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, room_name):
        ip = get_client_ip(request)
        geo_info = get_geolocation_for_ip(ip)

        try:
            channel = Channel.objects.get(location=geo_info["zip"])
        except:
            channel = Channel(name="dummy", location=geo_info["zip"])
            channel.save()
            channel.name = f"Channel #{channel.pk}"
            channel.save()
        request.user.channel = channel
        request.user.save()
        if channel.member_set.count() < 3:
            request.user.is_mod = True

        messages = channel.message_set.all()
        return render(request, "channelsapp/channels.html", {"room_name": room_name, "messages": messages})

    def post(self, request, pk):
        channel_code = request.POST.get("channel_code")
        message = request.POST.get("message")
        return redirect(
            '/play/%s?&message=%s' 
            %(channel_code, message)
        )
