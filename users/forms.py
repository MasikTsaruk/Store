from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, forms
from users.models import User, EmailVerification
import uuid
from datetime import timedelta
from django.utils.timezone import now
from .tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    class Meta:
       model = User
       fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password2', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image')
