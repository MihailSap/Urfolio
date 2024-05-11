import uuid

from django.db import models
import datetime

from django.urls import reverse
from users.models import User # Оно только так и работает, несмотря на красный





class ProjectCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ide = models.CharField(max_length=128, unique=True, default='abcd')
    def __str__(self):
        return self.name

class ProjectYear(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ide = models.CharField(max_length=128, unique=True,default='abcd')
    def __str__(self):
        return self.name

class ProjectCourseNumber(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ide = models.CharField(max_length=128, unique=True, default='abcd')
    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to='projects_images', null=True, blank=True)
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    date_publication = models.DateField(default= datetime.date.today)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes')

    category = models.ForeignKey(to=ProjectCategory, on_delete=models.CASCADE)
    year = models.ForeignKey(to=ProjectYear, on_delete=models.CASCADE)
    course_number = models.ForeignKey(to=ProjectCourseNumber, on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count() # ??? почему подчёркнуто
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.pk})

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














