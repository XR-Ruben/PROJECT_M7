from django.contrib import admin
from m7_python.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)

# Modificación de títulos en el Django Admin (opcional)
admin.site.site_header = "Arriendos.Com"
admin.site.index_title = "Bienvenidos al portal de Arriendos.Com"