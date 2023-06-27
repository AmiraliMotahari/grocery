from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser
    list_display = ['username','first_name','last_name','email','city','is_staff',] # new
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('city',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('city',)}),
    )

    
admin.site.register(CustomUser, CustomUserAdmin)
