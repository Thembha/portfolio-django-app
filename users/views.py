from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    template = "profile.html"
    context = {"user":user,"page":"profile"}
    return render(request,template,context)

def edit(request):

    return render(request, 'edit_profile.html', {"page":"edit"})

def map(request):
    users = User.objects.all()
    template = "map.html"
    context = {"users":users,"page":"map"}
    return render(request,template,context)