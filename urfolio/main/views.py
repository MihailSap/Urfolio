from .models import ProjectCategory, Project, ProjectYear, ProjectCourseNumber
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)


def index(request, category_id=None):
    projects = Project.objects.filter(category_id=category_id) if category_id else Project.objects.all()
    context = {
        'projects': projects,
        'years': ProjectYear.objects.all(),
        'course_numbers': ProjectCourseNumber.objects.all(),
        'categories': ProjectCategory.objects.all()
    }
    return render(request, 'main/main.html', context)

class ProjectDetailView(DetailView): # Так правильнее
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['image', 'name', 'description', 'category', 'year', 'course_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['image', 'name', 'description', 'category', 'year', 'course_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # Пользователь может редактировать только свои проекты
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectListView(ListView):
    model = Project
    template_name = 'main/main.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    #ordering = ['-date_posted'] - не рабочий способ сортировки по дате публикации

class ProjectDeleteView(UserPassesTestMixin, DeleteView): # Так правильнее
    model = Project
    success_url = '/'

    def test_func(self): # Пользователь может удалять только свои проекты
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False






