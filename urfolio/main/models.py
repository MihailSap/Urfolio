import uuid

from django.db import models
import datetime

from django.urls import reverse
from users.models import User # Оно только так и работает, несмотря на красный
from PIL import Image

class Project(models.Model):
    class Category(models.TextChoices):
        Сайт = 'Сайт';
        Игра = 'Игра';
        Мобильное_приложение = 'Мобильное приложение';
    class CourseNumber(models.TextChoices):
        Первый_курс = '1 курс';
        Второй_курс = '2 курс';
        Третий_курс = '3 курс';
        Четвёртый_курс = '4 курс';
    class Year(models.TextChoices):
        Год_2023_2024 = '2023-2024';
        Год_2022_2023 = '2022-2023';
        Год_2021_2022 = '2021-2022';
        Год_2020_2021 = '2020-2021';

    # Изображения
    image = models.ImageField(default='default-project.png', upload_to='projects_images')
    photo1 = models.ImageField(null=True, blank=True, upload_to='projects_images');
    photo2 = models.ImageField(null=True, blank=True, upload_to='projects_images');
    photo3 = models.ImageField(null=True, blank=True, upload_to='projects_images');
    photo4 = models.ImageField(null=True, blank=True, upload_to='projects_images');

    # Основная информация
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    members = models.TextField(null=True, blank=True)
    date_publication = models.DateField(default= datetime.date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes')
    slikess = models.ManyToManyField(User, related_name='likedposts', through='LikedPost')

    # Фильтры
    category = models.CharField(max_length=128, choices=Category.choices)
    course_number = models.CharField(max_length=128, choices=CourseNumber.choices)
    year = models.CharField(max_length=128, choices=Year.choices)

    # ССЫЛКИ НА СОЦ СЕТИ
    github_link = models.URLField(null=True, blank=True)
    figma_link = models.URLField(null=True, blank=True)
    vk_link = models.URLField(null=True, blank=True)
    tg_link = models.URLField(null=True, blank=True)
    cloud_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.pk})

    def total_comments_and_replies(self):
        total_comments = self.comments.count()
        total_replies = Reply.objects.filter(parent_comment__parent_project=self).count()
        return total_comments + total_replies


class LikedPost(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)
    def __str__(self):
        return f'{self.user.username} : {self.project.name}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['-created']

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['created']














