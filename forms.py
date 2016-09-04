from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import PlainUser
from registration.forms import RegistrationFormTermsOfService

class PlainUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta:
        model = PlainUser
        fields = ("email",)

class PlainUserChangeForm(UserChangeForm):

    class Meta:
        model = PlainUser
        fields = '__all__'

        
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

class CustomRegistrationForm(RegistrationFormTermsOfService):

    class Meta:
        model = PlainUser
        fields = tuple(['email'] + model.REQUIRED_FIELDS + ['password1', 'password2'])
   
    bad_domains = []

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.

        """
        email_domain = self.cleaned_data['email'].split('@')[1]

        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        elif PlainUser.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))

        return self.cleaned_data['email']

   

        
        


