from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('petition/', views.Petition.as_view(), name='petition'),
]