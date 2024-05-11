from django.forms import ModelForm
from django import forms
from main.models import Comment # ТАК ПРАВИЛЬНО ЗАПИСЫВАТЬ, НЕСМОТРЯ НА ПОДЧЁРКИВАНИЕ


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Поделитесь своим мнением'})
        }
        labels = {
            'body': ''
        }