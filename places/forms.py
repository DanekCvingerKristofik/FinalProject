from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


from places.models import Purchase, Profil


class PurchaseForm(ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'






class RegistrationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=True)
        Profil.objects.create(user=user)
        return user




