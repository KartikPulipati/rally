from django.shortcuts import render
from django.views import View
from ipware import get_client_ip
import requests
from .models import Channel
from django.conf import settings

def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key={settings.IP_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

class ChannelView(View):
    def get(self, request, pk):
        ip = get_client_ip(request)
        geo_info = get_geolocation_for_ip(ip)

        try:
            channel = Channel.objects.get(loctation=geo_info["zip"])
        except:
            channel = Channel(name="dummy", location=geo_info["zip"])
            channel.name = f"Channel #{channel.pk}"
            channel.save()

        breakpoint()
        if channel.member_set.count() < 3:
            request.user.is_mod = True
        request.user.channel = channel
        request.user.save()

        return render(request, "rallyapp/base.html", {"pk": pk})

    def post(self, request, pk):
        pass
