from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse, reverse_lazy
from .filters import ProjectFilter
from .forms import CommentCreateForm, ReplyCreateForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import (
    Project,
    Comment, Reply
)
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

def like_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    user_exist = project.slikess.filter(username=request.user.username).exists()
    if project.author != request.user:
        if user_exist:
            project.slikess.remove(request.user)
        else:
            project.slikess.add(request.user)
    return render(request, 'snippets/likes.html', {'project': project})

from django.shortcuts import render
from .models import Project
from .filters import ProjectFilter

def index(request):
    projects_qs = Project.objects.all()
    projects_filters = ProjectFilter(request.GET, queryset=projects_qs)

    # Check if the sorting parameters are present in the GET request
    sort_by = request.GET.get('sort', None)
    sort_order = request.GET.get('order', 'asc')  # Default to ascending order

    if sort_by == 'name':
        if sort_order == 'asc':
            projects_qs = projects_filters.qs.order_by('name')
            next_order = 'desc'
        else:
            projects_qs = projects_filters.qs.order_by('-name')
            next_order = 'asc'
    elif sort_by == 'slikess':
        if sort_order == 'asc':
            projects_qs = projects_filters.qs.order_by('slikess').annotate(count=Count('slikess')).order_by('-count')
            next_order = 'desc'
        else:
            projects_qs = projects_filters.qs.order_by('slikess').annotate(count=Count('slikess')).order_by('count')
            next_order = 'asc'
    else:
        projects_qs = projects_filters.qs
        next_order = 'asc'

    context = {
        'form': projects_filters.form,
        'projects': projects_qs,
        'next_order': next_order,
        'current_sort': sort_by,
    }
    return render(request, 'main/main.html', context)

# def index(request):
#     projects_qs = Project.objects.all()
#
#     # ПО НАЗВАНИЮ
#     # projects_qs = Project.objects.order_by('-name')
#     # ПО КОЛ-ВУ ЛАЙКОВ
#     #projects_qs = Project.objects.order_by('slikess').annotate(count=Count('slikess')).order_by('-count')
#
#     projects_filters = ProjectFilter(request.GET, queryset=projects_qs)
#     context = {
#         'form': projects_filters.form,
#         'projects': projects_filters.qs,
#     }
#     return render(request, 'main/main.html', context)

def sortByTitle(request):
    projects_qs = Project.objects.order_by('-name')
    projects_filters = ProjectFilter(request.GET, queryset=projects_qs)
    context = {
        'form': projects_filters.form,
        'projects': projects_filters.qs,
    }
    return render(request, 'main/main.html', context)

# def index(request):
#     sort_type = request.GET.get('sort_type', 'default')
#     if sort_type == 'slikess_desc':
#         projects = Project.objects.annotate(slikes_count=Count('slikess')).order_by('-slikes_count')
#     else:
#         projects = Project.objects.all()
#     return render(request, 'main/main.html', {'projects': projects})

@login_required
def comment_sent(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_project = project
            comment.save()
    return redirect('projects:project_detail', project.id) # или pk=project.id

@login_required
def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid(): # ??
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()
    return redirect('projects:project_detail', comment.parent_project.id) # или pk=project.id

@login_required
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comment, id=pk, author=request.user)
    parent_project_id = comment.parent_project.id
    comment.delete()
    return redirect('projects:project_detail', pk=parent_project_id)

@login_required
def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    parent_project_id = reply.parent_comment.parent_project.id
    reply.delete()
    return redirect('projects:project_detail', pk=parent_project_id)

def ProjectDeleteView(request, pk):
    project = get_object_or_404(Project, id=pk, author=request.user)
    if request.user == project.author:
        project.delete()
    return redirect(reverse_lazy('projects:index1'))

# ОТОБРАЖЕНИЕ ПРОЕКТА НА ОТДЕЛЬНОЙ СТРАНИЦЕ
class ProjectDetailView(DetailView): # Так правильнее
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        commentform = CommentCreateForm()
        replyform = ReplyCreateForm()
        context['commentform'] = commentform
        context['replyform'] = replyform
        return context

# СОЗДАНИЕ ПРОЕКТА
class ProjectCreateView(CreateView):
    model = Project
    fields = ['image', 'name', 'description', 'category', 'course_number', 'year']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# РЕДАКТИРОВАНЕ ПРОФИЛЯ
class ProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['image', 'name', 'description', 'category', 'course_number', 'year']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # Пользователь может редактировать только свои проекты
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False



# ОТОБРАЖЕНИЕ ПРОЕКТА НА ОБЩЕЙ СТРАНИЦЕ ( ОТКЛЮЧЕН! )
# class ProjectListView(ListView):
#     model = Project
#     template_name = 'main/main.html'
#     context_object_name = 'projects'
#     paginate_by = 3 # СКОЛЬКО ПРОЕКТОВ ПОКАЗЫВАТЬ НА ОДНОЙ СТРАНИЦЕ
