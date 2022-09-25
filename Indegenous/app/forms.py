from socket import fromshare
from django import forms
from .models import Element




class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Element
        fields=['Name','Text']
        widgets={'Name':forms.TextInput(attrs=
        {'class':'form-control'}),'Text':forms.TextInput(attrs=
        {'class':'form-control'})}