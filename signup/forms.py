from django import forms
from index.models import Data_user

class BiodataUser(forms.ModelForm):
    class Meta:
        model=Data_user
        fields="__all__"
        error_messages = {
            'firstname':{
                'required':'Anda Harus Mengisi Nama Depan'
            },
            'lastname':{
                'required':'Anda Harus Mengisi Nama Belakang'
            },
            'email':{
                'required':'Anda Harus Mengisi Email'
            },
            'password':{
                'required':'Anda Harus Mengisi Password'
            }
        }