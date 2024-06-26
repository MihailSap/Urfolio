from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import UserCreationForm, ProfileUpdateForm, UserUpdateForm
from main.models import Project
from .models import Profile, User

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('profile', kwargs={'username': username}))
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

def profile_management(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', username=request.user.username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_management.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        if user == request.user:
            profile = Profile.objects.create(user=user)
        else:
            profile = None  # Если профиля нет и пользователь не текущий, можно вернуть 404 или другое поведение

    projects = Project.objects.all()

    context = {
        'profile': profile,
        'projects': projects
    }

    if user == request.user:
        return render(request, 'users/profile.html', context)
    else:
        return render(request, 'users/guest_profile.html', context)

