from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import PlainUser

class PlainUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta:
        model = PlainUser
        fields = ("email", "first_name", "last_name",)

class PlainUserChangeForm(UserChangeForm):

    class Meta:
        model = PlainUser
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

