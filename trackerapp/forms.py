from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from trackerapp.models import TicketTracking, Feature


class RegisterForm(UserCreationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True, }))

    first_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})),
                                 max_length=30, required=False)

    last_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})),
                                max_length=30, required=False)

    email = forms.EmailField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})),
                             max_length=254)

    password1 = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
                               )
    password2 = forms.CharField(label=_("Confirm Password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2


class SignInForm(AuthenticationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True, }), )

    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               )

    class Meta:
        model = User

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class TicketCreationForm(forms.ModelForm):
    ticket_name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ticket_name', 'autofocus': True, }))

    ticket_comment = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ticket_comment'})),
                                 max_length=30, required=False)

    ticket_status = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ticket_status'})),
                                max_length=30, required=False)

    class Meta:
        model = TicketTracking
        fields = ('ticket_name', 'ticket_comment', 'ticket_status')

class FeatureCreationForm(forms.ModelForm):
    feature_name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Feature_name', 'autofocus': True, }))


    class Meta:
        model = Feature
        fields = ('feature_name',)

