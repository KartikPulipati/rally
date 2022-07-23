from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Petition, Signature
from .forms import PetitionForm

def home(request):
    return render(request, "rallyapp/home.html")


class PetitionView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        petitions = Petition.objects.all()
        return render(request, "rallyapp/petitions.html", {"petitions": petitions})

    def post(self, request):
        pass

def sign(request, pk):
    if not Signature.objects.filter(member=request.user, petition=Petition.objects.get(pk=pk)).exists():
        return render(request, "rallyapp/sign.html")

def view_petition(request, pk):
    petition = Petition.objects.get(pk=pk)
    signatures = Signature.objects.filter(petition=petition)
    return render(request, "rallyapp/view_petition.html", {"petition": petition, "signatures": signatures})

