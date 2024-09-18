from django.shortcuts import render, redirect, get_object_or_404
from .services import get_all_inmuebles, get_or_create_user_profile, create_inmueble_for_arrendador,  get_inmuebles_for_arrendador, actualizar_disponibilidad_inmueble
from django.contrib import messages
from django.views import View
from m7_python.services import create_user
from m7_python.forms import (ContactModelForm, CustomUserCreationForm, UserEditProfileForm, 
                            UserForm, UserProfileForm, InmuebleForm, EditDisponibilidadForm, UpdateSolicitudEstadoForm)
from .models import UserProfile, Contact, Inmueble, Solicitud, User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .decorators import rol_requerido

#* Route para manejo de NOT_AUTH
def not_authorized_view(request):
    return render(request, "not_authorized.html", {})



@login_required
def indexView(request):
    if request.user.is_authenticated:
        profile = get_or_create_user_profile(request.user)
        if profile.tipo == 'arrendador':
            messages.success(request, 'Bienvenido a --> Arriendos.Com!!!')
            return redirect('dashboard_arrendador')
        elif profile.tipo == 'arrendatario':
            return redirect('index_arrendatario')
        else: 
            return redirect('login')
        # inmuebles = get_all_inmuebles()
        # return render(request,'index.html',{'inmuebles':inmuebles} )
    else:
        return redirect('login')
    
    
@login_required   
def index_arrendatario(request):
    inmuebles = get_all_inmuebles()
    return render(request,'arrendatario/index_arrendatario.html',{'inmuebles':inmuebles} )

@login_required 
def dashboard_arrendador(request):
    inmuebles = get_inmuebles_for_arrendador(request.user)
    return render(request, 'arrendador/dashboard_arrendador.html', {'inmuebles': inmuebles})    



# class RegisterView(View):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def post(self, request):
#         username = request.POST['first_name']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         password_repeat = request.POST['password_repeat']
#         # Validación del passoword ingresado
#         if password != password_repeat:
#             messages.error(request, 'Las contraseñas no coinciden')
#             return render(request, 'registration/register.html')
#         try:
#             crear_usuario(username, first_name, last_name, email, password)
#         except IntegrityError:
#             messages.error(request, 'El correo ya existe')
#             return render(request, 'registration/register.html')
#         except Exception:
#             messages.error(request, 'No se ha podido registrar el usuario')
#             return render(request, 'registration/register.html')
#         # Si llega aquí, es porque no hubo errores.
#         messages.success(request, '¡Usuario creado con éxito! Por favor, ingrese')
#         return redirect('registration/register_rol.html')

#     def get(self, request):
#         return render(request, 'registration/register.html')
    

# STEP -> CREAR el FORM de Registro
#TODO__ REGISTER and REGISTER_ROL (tipo de usuario) - FORMS
def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_rol')
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form} )


class ContactView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get(self, request):
        form = ContactModelForm()                    
        context = {'form': form}               
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactModelForm(request.POST)        
        if form.is_valid():                     
            form.save()
            messages.success(request, 'Mensaje enviado con éxito')                                  
            return redirect('index')         
        context = {
	    'form': form
	    } 
        messages.error(request, 'No se ha podido enviar el mensaje')               
        return render(request, 'contact.html', context) 
    
@login_required
def register_rol(request):
    user_profile = get_or_create_user_profile(request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio o cualquier otra página
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/register_rol.html', {'form': form})    


#* VER PERFIL
@login_required
def profile_view(request):
    user = request.user
    user_profile = get_or_create_user_profile(user)  # Llama al servicio para obtener o crear el perfil

    if not user_profile:
        # En caso de que ocurra un error al obtener o crear el perfil
         return render(request, 'error.html', {'message': 'No se pudo obtener el perfil del usuario.'})

    return render(request, 'profile_detail.html', {
        'user': user,
         'profile': user_profile,
    })


@login_required
def edit_profile_view(request):
    user = request.user 
    user_profile = get_or_create_user_profile(user)
    tipo=user_profile.tipo
    if request.method == 'POST':
        print("hola estoy adentro")
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserEditProfileForm(request.POST, instance=user_profile) 
        # profile_form.tipo=tipo
        if user_form.is_valid() and profile_form.is_valid():
            print("hola estoy adentro de la validacion del formulario")
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else: # GET
        user_form = UserForm(instance=user) 
        profile_form = UserEditProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'tipo':tipo
    })

def about(request):
    return render(request, 'about.html', {})



#TODO__ ARRENDADOR - VIEWS

#* HITO 4

@login_required
@rol_requerido('arrendador')
def create_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = create_inmueble_for_arrendador(request.user, form.cleaned_data)
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm()
    return render(request, 'arrendador/create_inmueble.html', {'form': form})

@login_required
def edit_inmueble(request, inmueble_id):
    inmueble_edit =  get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble_edit =  Inmueble.objects.get(pk=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble_edit)
        if form.is_valid():
            #* Crear service para update Inmueble y validar
            form.save()
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm(instance=inmueble_edit)
    return render(request, 'arrendador/edit_inmueble.html', {'form': form})


@login_required
def detail_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble =  Inmueble.objects.get(id=inmueble_id)
    return render(request, 'detail_inmueble.html', {'inmueble': inmueble})


@login_required
def delete_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('dashboard_arrendador')

    return render(request, 'arrendador/delete_inmueble.html', {'inmueble': inmueble})



@login_required
def edit_disponibilidad_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = EditDisponibilidadForm(request.POST, instance=inmueble) 
        if form.is_valid():
            disponible = form.cleaned_data['disponible']
            result = actualizar_disponibilidad_inmueble(inmueble_id, disponible)
            if result["success"]:
                messages.success(request, result["message"])
            else: 
                messages.error(request, result["message"])
            return redirect('dashboard_arrendador')
             
    else: 
        form = EditDisponibilidadForm(instance=inmueble)
    return render(request, 'arrendador/edit_disponibilidad.html', {'form': form, 'inmueble': inmueble})



#TODO__ ARRENDATARIOS - VIEWS


@login_required
@rol_requerido('arrendatario')
def send_solicitud(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        solicitud = Solicitud(arrendatario= request.user, inmueble= inmueble, estado= 'pendiente')
        solicitud.save()
        messages.success(request, f'Solicitud inmueble {inmueble.nombre} realizada con éxito!!!')
        return redirect('index_arrendatario')
    return render(request, 'arrendatario/send_solicitud.html', {'inmueble': inmueble})
    
    


def view_list_user_solicitudes(request):
    
    arrendatario =  get_object_or_404(User, id=request.user.id)
    solicitudes = Solicitud.objects.filter(arrendatario=arrendatario)
    return render(request, 'arrendatario/list_user_solicitudes.html', {
        'solicitudes': solicitudes,
        'arrendatario': arrendatario
    })
    
    
    
#* del ARRENDADOR
@login_required
def view_list_solicitudes(request, inmueble_id):
    # Obtenemos inmueble para validar previamente
    inmueble = get_object_or_404(Inmueble, id=inmueble_id) 
    solicitudes = Solicitud.objects.filter(inmueble_id=inmueble_id)
    return render(request, 'arrendador/list_solicitudes.html', {'inmueble':inmueble, 'solicitudes': solicitudes})





@login_required
def edit_status_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id) 
    if request.method == 'POST':
        form = UpdateSolicitudEstadoForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            print(f'--> {form.cleaned_data['estado']}')
            return redirect('view_list_solicitudes', inmueble_id=solicitud.inmueble.id)
    else:
        form = UpdateSolicitudEstadoForm(instance=solicitud)
    return render(request, 'arrendador/edit_status_solicitud.html', {'form': form, 'solicitud': solicitud})    