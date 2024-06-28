from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse, reverse_lazy
from .filters import ProjectFilter
from .forms import CommentCreateForm, ReplyCreateForm, ProjectCreateForm
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
    return redirect(reverse_lazy('profile', kwargs={'username': request.user.username}))

# ОТОБРАЖЕНИЕ ПРОЕКТА НА ОТДЕЛЬНОЙ СТРАНИЦЕ
def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()
    context = {
        'project': project,
        'commentform': commentform,
        'replyform': replyform,
    }
    return render(request, 'main/project_detail.html', context)

# СОЗДАНИЕ ПРОЕКТА
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# РЕДАКТИРОВАНЕ ПРОЕКТА
def project_management(request, pk=None):
    if pk:
        project = get_object_or_404(Project, id=pk)
    else:
        project = None

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect(reverse('projects:project_detail', kwargs={'pk': project.id}))
    else:
        form = ProjectCreateForm(instance=project)

    context = {
        'form': form,
        'project': project
    }
    return render(request, 'main/project_form.html', context)


class ProjectListView(ListView):
    model = Project
    template_name = 'main/main.html'
    context_object_name = 'projects'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        projects_filters = ProjectFilter(self.request.GET, queryset=queryset)
        queryset = projects_filters.qs
        sort_by = self.request.GET.get('sort', None)
        sort_order = self.request.GET.get('order', 'asc')  # Default to ascending order

        if sort_by == 'name':
            if sort_order == 'asc':
                queryset = queryset.order_by('name')
            else:
                queryset = queryset.order_by('-name')
        elif sort_by == 'slikess':
            if sort_order == 'asc':
                queryset = queryset.annotate(count=Count('slikess')).order_by('count')
            else:
                queryset = queryset.annotate(count=Count('slikess')).order_by('-count')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort_by = self.request.GET.get('sort', None)
        sort_order = self.request.GET.get('order', 'asc')  # Default to ascending order
        next_order = 'asc' if sort_order == 'desc' else 'desc'
        current_order = 'desc' if sort_order == 'desc' else 'asc'
        projects_filters = ProjectFilter(self.request.GET, queryset=self.get_queryset())
        context.update({
            'form': projects_filters.form,
            'next_order': next_order,
            'current_sort': sort_by,
            'current_order': current_order
        })
        return context
