from django import forms
from django.forms import ModelForm
from m7_python.models import ContactForm, UserProfile, Inmueble, Contact, Solicitud
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'email', 'mensaje']
        labels = {
            'nombre': 'Nombre:',
            'Email': 'email',
            'mensaje': 'Mensaje'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'ej. Ruben Ramírez',
                }
            ),
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'ej. ruben@mail.com'
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Máximo 500 carácteres'
                }
            )
        }   


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono', 'tipo']

#TODO_ EDIT PROFILE -FORM
# UserProfileForm - este form nos va a servir además para cuando vayamos a editar el perfil
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono', 'tipo']
        # fields = ['rut', 'direccion', 'telefono'] --> quitar tipo para solucionar problema de guardar edicion de tipo de usuario



#TODO__ FORM INMUEBLE - CREAR 
class InmuebleForm(forms.ModelForm):
    class Meta: 
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales',
            'num_estacionamientos', 'num_habitaciones', 'num_baños',
            'direccion', 'tipo_inmueble', 'precio', 'disponible',
            'comuna'
        ]  
        
        
        
#TODO__ FORM DISPONIBILIDAD  

class EditDisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['disponible']  # Solo permitimos modificar la disponibilidad
        widgets = {
            'disponible': forms.CheckboxInput(),  # Input como checkbox (disponible o no)
        }
        
        
#TODO__ FORM SOLICITUDES 
class UpdateSolicitudEstadoForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['estado']
        widgets = {
            'estado': forms.Select(choices=Solicitud.ESTADOS)  # ChoiseField basado en el modelo
        }         