from django import forms
from . import models

class CandyForm(forms.ModelForm):
    class Meta:
        model = models.Candy
        fields = "__all__"