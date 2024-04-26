from django.db import models
import datetime

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
    image = models.ImageField(upload_to='projects_images')
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    date_publication = models.DateField(default= datetime.date.today)
    category = models.ForeignKey(to=ProjectCategory, on_delete=models.CASCADE)
    year = models.ForeignKey(to=ProjectYear, on_delete=models.CASCADE)
    course_number = models.ForeignKey(to=ProjectCourseNumber, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
