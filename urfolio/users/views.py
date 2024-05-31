from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


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
            username = form.cleaned_data.get('username') # ПАРОЛИ 8 СИМВОЛОВ МИНИМУМ, И ЦИФРЫ, И БУКВЫ
            password = form.cleaned_data.get('password1') # МОЖНО ЕМЭЙЛ!! email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

def profile_management(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    user_form = UserUpdateForm(instance=request.user)
    context = {'user_form': user_form}
    return render(request, 'users/profile_management.html', context)

def profile(request):
    return render(request, 'users/profile.html')










