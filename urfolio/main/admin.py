from django.contrib import admin
from .models import (
    Project, ProjectCategory,
    ProjectYear, ProjectCourseNumber,
    Comment, Reply,
)

# ПРОЕКТ
admin.site.register(Project)

# КОММЕНТАРИИ
admin.site.register(Comment)
admin.site.register(Reply)

# СТАРЫЕ ФИЛЬТРЫ
admin.site.register(ProjectCategory)
admin.site.register(ProjectYear)
admin.site.register(ProjectCourseNumber)
