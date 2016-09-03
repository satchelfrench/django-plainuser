'''
Admin configuration for PlainUser
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .forms import PlainUserChangeForm, PlainUserCreationForm
from .models import PlainUser


class PlainUserAdmin(UserAdmin):
    #user_fields = tuple(['email', 'password1', 'password2'] + PlainUser.REQUIRED_FIELDS)
    
        
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2')
        }
    ),
    )

    form = PlainUserChangeForm
    add_form = PlainUserCreationForm
    list_display = ('email', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register the a PlainUser
admin.site.register(PlainUser, PlainUserAdmin)

