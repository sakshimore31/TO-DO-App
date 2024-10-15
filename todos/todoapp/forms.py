from django import forms
from .models import Mytodo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model= User
        fields = ['first_name','last_name','username','email','password1','password2']

class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length = 50, widget=forms.TextInput(attrs = {
        'id': 'todoField', 'placeholder': 'Enter Task'
    }))
    class Meta:
        model = Mytodo
        fields = ['task',]