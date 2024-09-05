from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    tipos = (('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    tipo = models.CharField(max_length=255, choices=tipos, default='arrendatario')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.rol})'
    
class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'
    
    
class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.RESTRICT) 
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'      


# class Region(models.Model):
#     nombre_region = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nombre_region

# class Comuna(models.Model):
#     nombre_comuna = models.CharField(max_length=100)
#     id_region = models.ForeignKey(Region, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre_comuna

# class TipoUser(models.Model):
#     nombre_tipo_usuario = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nombre_tipo_usuario

# class User(models.Model):
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     rut = models.CharField(max_length=12, unique=True)
#     direccion = models.CharField(max_length=255)
#     telefono = models.CharField(max_length=15)
#     correo = models.EmailField(unique=True)
#     tipo_usuario = models.ForeignKey(TipoUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nombre} {self.apellido}"

class Inmueble(models.Model):
    TIPOS = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
    num_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    num_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.CharField(max_length=255, choices=TIPOS)
    precio = models.IntegerField(validators=[MinValueValidator(1000)], null=True)
    precio_ufs = models.FloatField(validators=[MinValueValidator(1.0)], null=True)
    disponible = models.BooleanField(default=True)
    #* UF se utiliza para ajustar los valores de contratos, precios y pagos para reflejar cambios en la inflación.
    #TODO_ FKs - llaves foráneas - 1:N
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    arrendador = models.ForeignKey(User, related_name='inmuebles', on_delete=models.RESTRICT)
    #* arrendador - propietario es un USER de de tipo rol 'arrendador' en el UserProfile
    # estado = models.CharField(max_length=255, choices=ESTADO) # <- 'nuevo', 'estrenar', 'viejo'
    # arrendador

# class Inmueble(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
#     m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
#     numero_estacionamientos = models.IntegerField()
#     numero_baños = models.IntegerField()
#     numero_habitaciones = models.IntegerField()
#     direccion = models.CharField(max_length=255)
#     cod_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
#     cod_region = models.ForeignKey(Region, on_delete=models.CASCADE)
#     tipo_inmueble = models.CharField(max_length=100)
#     precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
#     estado = models.CharField(max_length=50)
#     arrendatario = models.ForeignKey(User, related_name='solicitudes_arrendatario', on_delete=models.CASCADE)
#     disponible = models.BooleanField(default=True)

#     def __str__(self):
#         return self.nombre
    
    
class Solicitud(models.Model):
    ESTADOS = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'), ('finalizada', 'Finalizada'))
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes', on_delete=models.CASCADE)
    arrendatario = models.ForeignKey(User, related_name='solicitudes_arrendatario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='pendiente')
    
    
    
    """
c. Operaciones CRUD con Django ORM
Crear un objeto con el modelo:

nuevo_inmueble = Inmueble(
    nombre="Casa en el centro",
    descripcion="Hermosa casa de 3 habitaciones en el centro de la ciudad.",
    m2_construidos=120.50,
    m2_terreno=150.00,
    numero_estacionamientos=2,
    numero_baños=2,
    numero_habitaciones=3,
    direccion="Calle Principal 123",
    id_comuna=Comuna.objects.get(id_comuna=1),
    id_region=Region.objects.get(id_region=1),
    tipo_inmueble="Casa",
    precio_mensual=750.00,
    estado="Disponible",
    id_user=User.objects.get(id_user=1)
)
nuevo_inmueble.save()


Enlistar desde el modelo de datos:

inmuebles = Inmueble.objects.all()
for inmueble in inmuebles:
    print(inmueble.nombre, inmueble.precio_mensual)


Actualizar un registro en el modelo de datos:

inmueble = Inmueble.objects.get(id_inmueble=1)
inmueble.precio_mensual = 800.00
inmueble.save()


Borrar un registro del modelo de datos:

inmueble = Inmueble.objects.get(id_inmueble=1)
inmueble.delete()

    
    """

