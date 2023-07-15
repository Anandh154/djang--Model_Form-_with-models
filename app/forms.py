from django import forms
from app.models import *

class PersonModelForm(forms.ModelForm):
    class Meta:
        model=PersonForm
        fields='__all__'
        