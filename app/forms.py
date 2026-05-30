from django import forms

from .models import *
class weatherdf(forms.ModelForm):
    class Meta:
        model=City
        fields='__all__'
        labels={'name':''}
        widgets={'name':forms.TextInput(attrs={'placeholder':'Enter New City'})}

