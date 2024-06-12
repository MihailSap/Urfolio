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


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#
#
# class ProfileUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ['image', 'description',
#                   'vk_link', 'github_link', 'figma_link', 'tg_link', 'cloud_link']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={}), required=False)

    vk_link = forms.URLField(required=False)
    github_link = forms.URLField(widget=forms.URLInput(attrs={}), required=False)
    figma_link = forms.URLField(widget=forms.URLInput(attrs={}), required=False)
    tg_link = forms.URLField(widget=forms.URLInput(attrs={}), required=False)
    cloud_link = forms.URLField(widget=forms.URLInput(attrs={}), required=False)
    class Meta:
        model = Profile
        fields = ['image', 'description',
                  'vk_link', 'github_link', 'figma_link', 'tg_link', 'cloud_link']

class UpdateUserForm(): # НЕ ИСПОЛЬЗУЕТСЯ
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']















