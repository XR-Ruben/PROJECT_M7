from django.shortcuts import render, redirect
from .services import get_all_inmuebles, get_or_create_user_profile
from django.contrib import messages
from django.views import View
from m7_python.services import crear_usuario
from m7_python.forms import ContactModelForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import UserProfile

# Create your views here.
def indexView(request):
    inmuebles = get_all_inmuebles()
    return render(request,'index.html',{'inmuebles':inmuebles} )



class RegisterView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST['first_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        # Validación del passoword ingresado
        if password != password_repeat:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'registration/register.html')
        try:
            crear_usuario(username, first_name, last_name, email, password)
        except IntegrityError:
            messages.error(request, 'El correo ya existe')
            return render(request, 'registration/register.html')
        except Exception:
            messages.error(request, 'No se ha podido registrar el usuario')
            return render(request, 'registration/register.html')
        # Si llega aquí, es porque no hubo errores.
        messages.success(request, '¡Usuario creado con éxito! Por favor, ingrese')
        return redirect('registration/register_rol.html')

    def get(self, request):
        return render(request, 'registration/register.html')
    

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
            return redirect('inicio')  # Redirige a la página de inicio o cualquier otra página
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/register_rol.html', {'form': form})    


#* VER PERFIL
@login_required
def profile_view(request):
    user = request.user
    # user_profile = get_or_create_user_profile(user)  # Llama al servicio para obtener o crear el perfil

    if not user_profile:
        # En caso de que ocurra un error al obtener o crear el perfil
        # return render(request, 'error.html', {'message': 'No se pudo obtener el perfil del usuario.'})

        return render(request, 'profile_detail.html', {
        'user': user,
        # 'profile': user_profile,
    })



def about(request):
    return render(request, 'about.html', {})