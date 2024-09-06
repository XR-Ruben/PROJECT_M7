from django.urls import path
from .views import indexView, RegisterView

urlpatterns = [
    path('', indexView, name='index'),
    path('registro/', RegisterView.as_view(), name='register'),

]