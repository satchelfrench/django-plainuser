'''
Admin configuration for PlainUser
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .forms import PlainUserChangeForm, PlainUserCreationForm
from django.utils.module_loading import import_string
from django.conf import settings

USER_MODEL_PATH = getattr(settings, 'USER_MODEL_PATH', 'accounts.models.PlainUser')
AUTH_USER_MODEL = import_string(USER_MODEL_PATH)

class PlainUserAdmin(UserAdmin):
    #user_fields = tuple(['email', 'password1', 'password2'] + PlainUser.REQUIRED_FIELDS)
    
        
    fieldsets = (
        (None, {'fields': tuple(['email', 'password'] + AUTH_USER_MODEL.REQUIRED_FIELDS)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': tuple(['email','password1', 'password2'] + AUTH_USER_MODEL.REQUIRED_FIELDS)
        }
    ),
    )

    form = PlainUserChangeForm
    add_form = PlainUserCreationForm
    list_display = ('email', 'is_staff', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register the a PlainUser
admin.site.register(AUTH_USER_MODEL, PlainUserAdmin)

