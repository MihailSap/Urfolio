from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy

from .models import Profile

User = get_user_model()

class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Придумайте пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description']

class UpdateUserForm():
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']















