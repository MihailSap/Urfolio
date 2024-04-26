from django.shortcuts import render
from .models import ProjectCategory, Project, ProjectYear, ProjectCourseNumber

def index(request, category_id=None):
    projects = Project.objects.filter(category_id=category_id) if category_id else Project.objects.all()
    context = {
        'projects': projects,
        'years': ProjectYear.objects.all(),
        'course_numbers': ProjectCourseNumber.objects.all(),
        'categories': ProjectCategory.objects.all()
    }
    return render(request, 'main/main.html', context)
