from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from bord.models import Profile, User, Skill
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Вход выполнен успешно!')
            else:
                return HttpResponse('Ошибка при авторизации')
        else:
            return HttpResponse('Неизвестный логин')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user, id=new_user.id)

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', pk=request.user.id)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def profile(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    return render(request, 'account/profile.html', {'user' : user})
