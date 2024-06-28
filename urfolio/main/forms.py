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

    photo1 = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'standart-input image-input',
            'placeholder': 'Загрузите изображение проекта',
            'type': 'file',
            'id': 'second',
            'name': 'file'
        }),
        required=False
    )
    photo2 = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'standart-input image-input',
            'placeholder': 'Загрузите изображение проекта',
            'type': 'file',
            'id': 'third',
            'name': 'file'
        }),
        required=False
    )
    photo3 = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'standart-input image-input',
            'placeholder': 'Загрузите изображение проекта',
            'type': 'file',
            'id': 'fourth',
            'name': 'file'
        }),
        required=False
    )
    photo4 = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'standart-input image-input',
            'placeholder': 'Загрузите изображение проекта',
            'type': 'file',
            'id': 'fourth',
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
    members = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'standart-input descript',
            'placeholder': 'Перечислите участников проекта'
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
        model = Project
        fields = ['image', 'photo1', 'photo2', 'photo3', 'photo4',
                  'name', 'description', 'members',
                  'category', 'course_number', 'year',
                  'vk_link', 'github_link', 'figma_link', 'tg_link', 'cloud_link']
