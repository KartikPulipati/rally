from django.shortcuts import render
from django.views import View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, "rallyapp/home.html")


class Petition(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):

        return render(request, "rallyapp/petition.html")

    def post(self, request):
        pass

def sign(request):
    
    return render(request, "rallyapp/sign.html")
