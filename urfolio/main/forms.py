from django.forms import ModelForm
from django import forms
from main.models import Comment, Reply # ТАК ПРАВИЛЬНО ЗАПИСЫВАТЬ, НЕСМОТРЯ НА ПОДЧЁРКИВАНИЕ


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

class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Добавьте ответ', 'class': "!text-sm"})
        }
        labels = {
            'body': ''
        }

from django import forms
from .models import Project

class ProjectCreateForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'standart-input image-input',
            'placeholder': 'Загрузите изображение проекта',
            'type': 'file',
            'id': 'first',
            'name': 'file'
        }),
        required=False
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'standart-input',
            'placeholder': 'Введите название проекта'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'standart-input descript',
            'placeholder': 'Введите описание проекта'
        }),
        required=False
    )
    category = forms.ChoiceField(
        choices=Project.Category.choices,
        widget=forms.Select(attrs={
            'class': 'standart-input',
            'placeholder': 'Выберите категорию проекта'
        })
    )
    course_number = forms.ChoiceField(
        choices=Project.CourseNumber.choices,
        widget=forms.Select(attrs={
            'class': 'standart-input',
            'placeholder': 'Выберите номер курса'
        })
    )
    year = forms.ChoiceField(
        choices=Project.Year.choices,
        widget=forms.Select(attrs={
            'class': 'standart-input',
            'placeholder': 'Выберите год'
        })
    )

    class Meta:
        model = Project
        fields = ['image', 'name', 'description', 'category', 'course_number', 'year']
