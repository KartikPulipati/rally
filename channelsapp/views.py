from django.shortcuts import render
from django.views import View
from ipware import get_client_ip
import requests
from django.conf import settings

def get_geolocation_for_ip(ip):
    print(ip)
    url = f"http://api.ipstack.com/{ip}?access_key={settings.IP_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

class ChannelView(View):
    def get(self, request, pk):
        geo_info = get_geolocation_for_ip(get_client_ip(request))
        print(geo_info)
        return render(request, "rallyapp/base.html", {"pk": pk})

    def post(self, request, pk):
        pass
