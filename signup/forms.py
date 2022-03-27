from django import forms
from index.models import Data_user

class BiodataUser(forms.ModelForm):
    class Meta:
        model=Data_user
        fields="__all__"
