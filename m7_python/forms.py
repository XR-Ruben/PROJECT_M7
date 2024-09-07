# from django import forms
# from .models import ContactForm
# from django.contrib.auth.models import User
# from .models import Profile
# from django.contrib.auth.forms import UserCreationForm


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