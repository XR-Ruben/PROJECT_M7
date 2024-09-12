from django.urls import path
from .views import indexView, RegisterView, ContactView, register_rol, profile_view, about, edit_profile_view
from . import views

urlpatterns = [
    path('', indexView, name='index'),
    path('accounts/register', RegisterView, name='register'),
    path('contacto/', ContactView.as_view(), name='contact'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('about/', about, name='about'),
    
    
]