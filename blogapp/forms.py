from django import forms 
from django.forms import ModelForm,TextInput,EmailInput,PasswordInput,Textarea
from .models import Blogmodel,commentmodel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class blogform(ModelForm):
    #title=forms.CharField(max_length=200,  widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    #Newpost=forms.CharField(max_length=200,widget=forms.Textarea)
    class Meta:
        model=Blogmodel
        fields='__all__'
        widgets={
            'title':TextInput(attrs={
                'placeholder':'title'
            }),
            'Newpost':Textarea(attrs={'placeholder':'Write something here'}),
            'summary':TextInput(attrs={'placeholder':'Write summary '}),
            
        }

class signupform(UserCreationForm):
    email=forms.EmailField(max_length=50,help_text='Required',widget=forms.EmailInput(attrs={'placeholder':'email'}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'Re Enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':TextInput(attrs={'placeholder':'username'})
        }
   # def __init__(self):
       # super().__init__()
        #self.fields['username'].widget.attrs['placeholder'] = 'Username'
        #self.fields['email'].widget.attrs['placeholder'] = 'Email'
        #self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        #self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class commentform(ModelForm):
  class Meta:
     model=commentmodel
     fields='__all__'
     widgets={
         'comment':TextInput(attrs={'placeholder':'add a comment'})
     }

