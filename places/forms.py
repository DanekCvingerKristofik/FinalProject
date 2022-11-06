from django import forms
from django.forms import ModelForm


from places.models import Purchase


class PurchaseForm(ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'

# class ProfilForm(ModelForm):
#     class Meta:
#         model = Profil
#         fields = '__all__'






