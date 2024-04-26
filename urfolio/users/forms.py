from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'Email'})
    )

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')



