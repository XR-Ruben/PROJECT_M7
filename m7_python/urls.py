from django.urls import path
from .views import indexView, RegisterView, ContactView
from . import views

urlpatterns = [
    path('', indexView, name='index'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('contacto/', ContactView.as_view(), name='contact'),
    
    
]