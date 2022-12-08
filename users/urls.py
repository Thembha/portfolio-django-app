from django.urls import path
from django.contrib.auth import views as auth_views
from . views import index, index_from_map, edit, map, RegisterView

urlpatterns = [
    path('', index, name='index'),
    path('profile/<user_id>/', index_from_map, name='index_from_map'),
    path('edit/', edit, name='edit'),
    path('map/', map, name='map'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='registration'), 
]