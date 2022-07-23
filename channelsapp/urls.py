from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:room_name>', views.ChannelView.as_view(), name='channel'),
    path('create-poll', views.create_poll, name='create-poll'),
    path('poll-vote', views.poll_vote, name='poll-vote'),
]