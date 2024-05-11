from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommentCreateForm, ReplyCreateForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import (
    ProjectCategory, Project,
    ProjectYear, ProjectCourseNumber,
    Comment, Reply
)
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

# ФУНКЦИЯ ДОБАВЛЕНИЯ ЛАЙКОВ
def LikeView(request, pk): # OLD
    project = get_object_or_404(Project, id=request.POST.get('project_id'))

    is_liked = False
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        is_liked = False
    else:
        project.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('projects:project_detail', args=[str(pk)]))

def like_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    user_exist = project.slikess.filter(username=request.user.username).exists()
    if project.author != request.user:
        if user_exist:
            project.slikess.remove(request.user)
        else:
            project.slikess.add(request.user)
    return render(request, 'snippets/likes.html', {'project': project})


def index(request, category_id=None):
    projects = Project.objects.filter(category_id=category_id) if category_id else Project.objects.all()
    context = {
        'projects': projects,
        'years': ProjectYear.objects.all(),
        'course_numbers': ProjectCourseNumber.objects.all(),
        'categories': ProjectCategory.objects.all()
    }
    return render(request, 'main/main.html', context)

# ОТОБРАЖЕНИЕ ПРОЕКТА НА ОТДЕЛЬНОЙ СТРАНИЦЕ
class ProjectDetailView(DetailView): # Так правильнее
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Project, id=self.kwargs['pk'])

        total_likes = stuff.total_likes()
        commentform = CommentCreateForm()
        replyform = ReplyCreateForm()

        is_liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            is_liked = True

        context['project'] = stuff
        context['commentform'] = commentform
        context['replyform'] = replyform
        context['total_likes'] = total_likes
        context['is_liked'] = is_liked
        return context




@login_required
def comment_sent(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid(): # ??
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

    if request.method == "POST":
        comment.delete()
        return redirect('projects:project_detail', comment.parent_project.id)

    return render(request, 'main/comment_delete.html', {'comment': comment})

@login_required
def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)

    if request.method == "POST":
        reply.delete()
        return redirect('projects:project_detail', reply.parent_comment.parent_project.id)

    return render(request, 'main/comment_delete.html', {'reply': reply})

# СОЗДАНИЕ ПРОЕКТА
class ProjectCreateView(CreateView):
    model = Project
    fields = ['image', 'name', 'description', 'category', 'year', 'course_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# РЕДАКТИРОВАНЕ ПРОФИЛЯ
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

# ОТОБРАЖЕНИЕ ПРОЕКТА НА ОБЩЕЙ СТРАНИЦЕ
class ProjectListView(ListView):
    model = Project
    template_name = 'main/main.html'
    context_object_name = 'projects'
    paginate_by = 3 # СКОЛЬКО ПРОЕКТОВ ПОКАЗЫВАТЬ НА ОДНОЙ СТРАНИЦЕ



# УДАЛЕНИЕ ПРОЕКТА
class ProjectDeleteView(UserPassesTestMixin, DeleteView): # Так правильнее
    model = Project
    success_url = '/'

    def test_func(self): # Пользователь может удалять только свои проекты
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False






