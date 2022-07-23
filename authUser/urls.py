from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signUp'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]