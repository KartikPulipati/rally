from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Petition, Signature
from .forms import PetitionForm
from django.db.models import Count

def home(request):
    return render(request, "rallyapp/home.html")

class PetitionView(View):

    def get(self, request):
        petitions = Petition.objects.annotate(count=Count("signature__id")).order_by("-count")
        signed_petitions = petitions.select_related('created_by').filter(signature__member=request.user)
        return render(request, "rallyapp/petitions.html", {"petitions": petitions, "signed_petitions": signed_petitions})

    def post(self, request):
        pass

class PetitionCreateView(FormView):
    template_name = "rallyapp/petition_create.html"
    form_class = PetitionForm
    success_url = "/petition"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)


def sign_petition(request):
    pk = request.POST["petition_id"]
    if not Signature.objects.filter(member=request.user, petition=Petition.objects.get(pk=pk)).exists():
        Signature.objects.create(member=request.user, petition=Petition.objects.get(pk=pk))
    return HttpResponse(status=204)

def view_petition(request, pk):
    petition = Petition.objects.get(pk=pk)
    signatures = Signature.objects.filter(petition=petition)
    return render(request, "rallyapp/view_petition.html", {"petition": petition, "signatures": signatures})

