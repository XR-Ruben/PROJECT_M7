from django.contrib import admin
from m7_python.models import UserProfile, Contact, Region, Comuna, Inmueble, Solicitud

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
	  pass
	
admin.site.register(Contact, ContactAdmin)

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Inmueble)
admin.site.register(Solicitud)

# Modificación de títulos en el Django Admin (opcional)
admin.site.site_header = "Arriendos.Com"
admin.site.index_title = "Bienvenidos al portal de Arriendos.Com"