from django.contrib import admin
from .models import Project, ProjectCategory, ProjectYear, ProjectCourseNumber

admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(ProjectYear)
admin.site.register(ProjectCourseNumber)


