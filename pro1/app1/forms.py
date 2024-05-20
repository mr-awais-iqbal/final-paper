from django import forms
from . models import *

class formView(forms.ModelForm):
    class Meta:
        model = book
        fields = ("__all__") 
        