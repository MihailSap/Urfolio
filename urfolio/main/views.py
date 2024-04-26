from django.shortcuts import render
from django.views.generic import View

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

class ProjectDetail(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        return render(request, 'main/project_detail.html', {'project': project})









