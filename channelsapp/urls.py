from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>', views.ChannelView.as_view(), name='channel'),
]