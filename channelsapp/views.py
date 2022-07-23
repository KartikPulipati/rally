from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ipware import get_client_ip
import requests
from .models import Channel, Poll, Choice
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
        request.user.save()

        messages = channel.message_set.all()
        return render(request, "channelsapp/channels.html", {"room_name": room_name, "messages": messages, "polls": channel.poll_set.all()})

    def post(self, request, pk):
        pass

def create_poll(request):
    channel = request.user.channel
    poll = Poll.objects.create(prompt=request.POST["prompt"], channel=channel)
    choices = []
    for i in request.POST["options"].replace("\r", "").split("\n"):
        if not i: continue
        choices.append(Choice(choice=i, poll=poll))
    Choice.objects.bulk_create(choices)
    return redirect("channel", room_name=channel.pk)
