from django import forms
from django.forms import ModelForm


from places.models import Purchase


class PurchaseForm(ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'




# class PurchaseForm(forms.Form):
#     trip= models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="purchases")
#     amount_adults= forms.IntegerField()
#     amount_children = forms.IntegerField()

