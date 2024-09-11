from django.urls import path
from .views import indexView, RegisterView, ContactView, register_rol, profile_view, about
from . import views

urlpatterns = [
    path('', indexView, name='index'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('contacto/', ContactView.as_view(), name='contact'),
    path('registration/register_rol', register_rol, name='register_rol'),
    path('profile/', profile_view, name='profile'),
    path('about/', about, name='about'),
    
    
]