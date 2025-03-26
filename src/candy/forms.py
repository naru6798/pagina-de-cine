from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm

class CandyForm(forms.ModelForm):
    class Meta:
        model = models.Candy
        fields = "__all__"

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]
