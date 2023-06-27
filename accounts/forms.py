from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm): 
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','city',)

class CustomUserChangeForm(UserChangeForm):
    
    class Meta: 
        model = CustomUser 
        fields = UserChangeForm.Meta.fields