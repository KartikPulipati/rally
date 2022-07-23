from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('petition/', views.PetitionView.as_view(), name='petition'),
    path('petition/<int:pk>/sign', views.sign, name='sign'),

]