from django import forms
from .models import Petition, Signature

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['name', 'description']