from django.urls import path
from .views import (indexView, RegisterView, ContactView, register_rol, 
                    profile_view, about, edit_profile_view, index_arrendatario, 
                    dashboard_arrendador, not_authorized_view, create_inmueble, 
                    edit_inmueble, detail_inmueble, delete_inmueble, edit_disponibilidad_inmueble, send_solicitud, view_list_user_solicitudes)

urlpatterns = [
    path('', indexView, name='index'),
    path('not_authorized/', not_authorized_view, name='not_authorized'),
    path('accounts/register', RegisterView, name='register'),
    path('contacto/', ContactView.as_view(), name='contact'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('about/', about, name='about'),
        # TODO__ PATH (urls - ROUTES) - ARRENDATARIO
    path('index', index_arrendatario, name='index_arrendatario'),
    path('inmueble/solicitar/<int:inmueble_id>/', send_solicitud, name='send_solicitud'),
    path('list/solicitudes/', view_list_user_solicitudes, name='solicitudes'),
#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

    # TODO__ PATH (urls - ROUTES) - ARRENDADOR
    path('dashboard', dashboard_arrendador, name="dashboard_arrendador"),
    path('dashboard/create', create_inmueble, name="create_inmueble"),
    path('dashboard/inmueble/edit/<int:inmueble_id>/',edit_inmueble, name='edit_inmueble'),
    path('dashboard/detail/<int:inmueble_id>/', detail_inmueble, name="detail_inmueble"),
    path('dashboard/inmueble/delete/<int:inmueble_id>/',delete_inmueble, name='delete_inmueble'),
    path('dashboard/inmueble/disponibilidad/<int:inmueble_id>/', edit_disponibilidad_inmueble, name='edit_disponibilidad_inmueble'),
    
    
]