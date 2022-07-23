from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ipware import get_client_ip
import requests
from .models import Channel, Poll, Choice, UserVote
from django.conf import settings


class ChannelView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, room_name):
        channel = request.user.channel
        messages = channel.message_set.all()
        show_poll_pks = [int(i) for i in request.user.uservote_set.all().values_list('poll', flat=True)]
        return render(request, "channelsapp/channels.html",
                      {"room_name": room_name, "messages": messages, "polls": channel.poll_set.all(),
                       "show_poll_pks": show_poll_pks})


def create_poll(request):
    channel = request.user.channel
    poll = Poll.objects.create(prompt=request.POST["prompt"], channel=channel)
    choices = []
    for i in request.POST["options"].replace("\r", "").split("\n"):
        if not i.strip(): continue
        choices.append(Choice(choice=i, poll=poll))
    Choice.objects.bulk_create(choices)
    return redirect("channel", room_name=channel.pk)


def poll_vote(request):
    UserVote.objects.create(user=request.user, poll=Poll.objects.get(pk=request.POST["poll_id"]))
    a = Choice.objects.get(pk=request.POST["choice_id"])
    a.votes += 1
    a.save()
    return HttpResponse(status=204)
