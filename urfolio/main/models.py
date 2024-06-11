import uuid

from django.db import models
import datetime

from django.urls import reverse
from users.models import User # Оно только так и работает, несмотря на красный


class Project(models.Model):
    class Category(models.TextChoices):
        WEBSITE = 'WEBSITE';
        NOVELL = 'NOVELL';
        MOBILE_APP = 'MOBILE_APP';
    class CourseNumber(models.TextChoices):
        FIRST = 'FIRST';
        SECOND = 'SECOND';
        THIRD = 'THIRD';
        FOURTH = 'FOURTH';
    class Year(models.TextChoices):
        FIRST = 'FIRST';
        SECOND = 'SECOND';
        THIRD = 'THIRD';
        FOURTH = 'FOURTH';
    image = models.ImageField(upload_to='projects_images', null=True, blank=True)
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    date_publication = models.DateField(default= datetime.date.today)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    likes = models.ManyToManyField(User, related_name='likes')
    slikess = models.ManyToManyField(User, related_name='likedposts', through='LikedPost')

    category = models.CharField(max_length=128, choices=Category.choices)
    course_number = models.CharField(max_length=128, choices=CourseNumber.choices)
    year = models.CharField(max_length=128, choices=Year.choices)

    # def total_likes(self):
    #     return self.likes.count()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.pk})


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














