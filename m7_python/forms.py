from django import forms
from django.forms import ModelForm
from m7_python.models import Contact, UserProfile
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

# #*  --- apply ContactFormForm --- 

# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(label='Correo')
#     customer_name = forms.CharField(max_length=64, label='Nombre')
#     message = forms.CharField(label='Mensaje')

# #*  --- apply ContactModelForm ---

# class ContactModelForm(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = ['customer_email', 'customer_name', 'message']
        
        
# #* PROFILE FORMS 
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'location', 'birth_date']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']   
        
        
# #* REGISTER FORMS  

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Este correo electrónico ya está en uso.")
#         return email      