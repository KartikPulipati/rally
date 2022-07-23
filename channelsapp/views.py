from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ipware import get_client_ip
import requests
from .models import Channel
from django.conf import settings

def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={settings.IP_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

class ChannelView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
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

        return render(request, "rallyapp/base.html", {"pk": pk})

    def post(self, request, pk):
        pass
