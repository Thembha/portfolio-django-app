from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from pprint import pprint
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = "profile.html"
    context = {"user":request.user,"page":"profile"}
    return render(request,template,context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='index')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form,"page":"edit"})

@login_required
def map(request):
    users = User.objects.all()
    template = "map.html"
    context = {"users":users,"page":"map"}
    return render(request,template,context)