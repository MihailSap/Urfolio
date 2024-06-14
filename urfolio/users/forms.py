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
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя',
        'id':'name',
        'class': 'standart-input',
        'name':'user-name'
    }))
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'type': 'file',
        'name': 'file',

    }), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'descript',
        'class': 'standart-input descript',
        'placeholder': 'Введите описание профиля'
    }), required=False)

    vk_link = forms.URLField(widget=forms.URLInput(attrs={
        'id': 'name',
        'placeholder': 'Добавьте ссылку на Ваш аккаунт в VK',
        'class': 'standart-input'
    }), required=False)
    github_link = forms.URLField(widget=forms.URLInput(attrs={
        'id': 'name',
        'placeholder': 'Добавьте ссылку на Ваш аккаунт в GitHub',
        'class': 'standart-input'
    }), required=False)
    figma_link = forms.URLField(widget=forms.URLInput(attrs={
        'id': 'name',
        'placeholder': 'Добавьте ссылку на Ваш аккаунт в Figma',
        'class': 'standart-input'
    }), required=False)
    tg_link = forms.URLField(widget=forms.URLInput(attrs={
        'id': 'name',
        'placeholder': 'Добавьте ссылку на Ваш аккаунт в Telegram',
        'class': 'standart-input'
    }), required=False)
    cloud_link = forms.URLField(widget=forms.URLInput(attrs={
        'id': 'name',
        'placeholder': 'Добавьте ссылку на Ваш аккаунт в облаке',
        'class': 'standart-input'
    }), required=False)
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















