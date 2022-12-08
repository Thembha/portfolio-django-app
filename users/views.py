from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from pprint import pprint
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import RegisterForm

def profile(req,user):
    template = "profile.html"
    context = {"user":user,"page":"profile"}
    return render(req,template,context)

@login_required
def index(request):
    return profile(request,request.user)

@login_required
def index_from_map(request,user_id):
    user = User.objects.get(pk=user_id)
    return profile(request,user)

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
    markers = []
    for user in users:
        if user.profile.location_lat and user.profile.location_lon:
            markers.append(
                {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "url": "profile/"+str(user.id),
                    "lat": str(user.profile.location_lat),
                    "lon": str(user.profile.location_lon),
                    "phone_number": user.profile.phone_number,
                    "home_address": user.profile.home_address,
                }
            )
    template = "map.html"
    context = {"markers":markers,"page":"map"}
    return render(request,template,context)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})