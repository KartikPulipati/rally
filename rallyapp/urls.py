from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('petition/', views.PetitionView.as_view(), name='petition'),
    path('petition/create', views.PetitionCreateView.as_view(), name='petition-create'),
    path('petition/<int:pk>/sign', views.sign, name='sign'),
    path('petition/<int:pk>/view', views.view_petition, name='view_petition'),
]