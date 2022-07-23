from django.urls import path, include
from . import views

urlpatterns = [
    path('channels/<int:room_name>', views.ChannelView.as_view(), name='channel'),
]