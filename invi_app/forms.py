from django import forms
from django.forms import ModelForm
from .models import User

class SignupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('user_email','password')
        widgets = {
            'password' : forms.PasswordInput
        }
        labels = {
           
            'user_email': '이메일',
            'password': '패스워드'
        }
       
class SigninForm(forms.ModelForm): #로그인을 제공하는 class이다.
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        exclude = ['user_name']