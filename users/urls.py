from django.urls import path

from . views import index, edit, map

urlpatterns = [
    path('', index, name='index'),
    path('edit/', edit, name='edit'),
    path('map/', map, name='map'),
]