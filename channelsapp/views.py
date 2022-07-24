from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Poll, Choice, UserVote


class ChannelView(View):

    def get(self, request, room_name):
        if not request.user.is_authenticated:
            return redirect('login')
        channel = request.user.channel
        messages = channel.message_set.all()
        show_poll_pks = [int(i) for i in request.user.uservote_set.all().values_list('poll', flat=True)]
        return render(request, "channelsapp/channels.html",
                      {"room_name": room_name, 'channel': channel, "messages": messages, "polls": channel.poll_set.all(),
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
