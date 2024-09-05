# PROYECTO - INMUEBLE

## HITO 1

1. Iniciar Proyecto
2. Implementar postgres SQL
3. Crear los modelos
4. Crear 4 servicios en nuestro services.py

## HITO 2

1. Poblar de datos nuestra DB (data semilla - load-data)
2. Testeo de nuestra DB desde el temp.py, de dos maneras:
   - Con ORM
   - Sin ORM (a pura consulta SQL)
   - Vamos a escribir los resultados en un data.txt

## HITO 3

1. Formularios
   - Registro
   - Inicio sesión
   - Alguna vista simple

## HITO 4

1. Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.

   - a. Generar las rutas para la vista para agregar nuevas viviendas.
   - b. Generar el objeto de formulario.
   - c. Agregar la función para guardar el objeto.

2. Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble existente.

   - a. Generar las rutas para la vista para actualizar las viviendas por usuario.
   - b. Generar el objeto de formulario en base a él modelo definido.
   - c. Agregar la función para actualizar el objeto.

3. Crear una página web básica donde los arrendatarios puedan ver la oferta disponible.
   - a. Generar las rutas para ver las viviendas.
   - b. Crear la vista y el controlador que le permitan enlistar las viviendas.

---

# VISTAS

- LandingPage de Bienvenida con Registrarme || Iniciar Sesión
  - Select para determinar TIPO_USUARIO (rol)
- Dashboard_arrendatario || Dashboard_arrendador
  - Ambos deben tener para editar su perfil
  - Vista lista

## PROPIETARIO - ARRENDADOR

- Vista de lista de sus publicaciones
- Vista detalle de inmueble
  - Lista de solicitudes (arrendatarios) de dicho inmueble con bttn para pasar de `pendiente` a `aprobado` o `rechazado`

1. Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.
   a. Generar las rutas para la vista para agregar nuevas viviendas.
   b. Generar el objeto de formulario.
   c. Agregar la función para guardar el objeto.

2. Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble
   existente.
   a. Generar las rutas para la vista para actualizar las viviendas por usuario.
   b. Generar el objeto de formulario en base a él modelo definido.
   c. Agregar la función para actualizar el objeto.

## INQUILINO - ARRENDATARIO

- Vista de inmuebles publicados
- Detalle de inmueble
  - Formulario de solicitud para dicho inmueble

3. Crear una página web básica donde los arrendatarios puedan ver la oferta disponible.
   a. Generar las rutas para ver las viviendas.
   b. Crear la vista y el controlador que le permitan enlistar las viviendas.

   # SERVICES + CONSULTAS

from django.contrib.auth.models import User
from .models import UserProfile

# Suponiendo que ya tienes un objeto de User creado.

nuevo_usuario = {
'username': 'Usuario1',
'email': 'juan@example.com',
'first_name': 'Juan',
'last_name': 'Vasquez',
'password': 'contraseña_segura123'
}

usuario = create_user(nuevo_usuario)
print(usuario)

# Crear una Región:

from .models import Region

region = Region.objects.create(
cod='01',
nombre='Región Metropolitana'
)

# Crear una Comuna:

from tu_app.models import Region, Comuna

# Obtener la región con código '001'

region = Region.objects.get(cod='01')

# Crear una comuna asociada a la región

nueva_comuna = Comuna(cod='1001', nombre='Santiago Centro', region=region)
nueva_comuna.save()

# Crear un Inmueble:

from .models import Inmueble, Comuna
from django.contrib.auth.models import User

comuna = Comuna.objects.get(cod='1001')
arrendador = User.objects.get(username='Usuario1')

data = {
'id_user': 1,  
 'tipo_inmueble': 'Apartamento',
'comuna_cod': '002',  
 'nombre': 'Apartamento Moderno',
'descripcion': 'Un apartamento en pleno centro de la ciudad',
'm2_totales': 150,
'm2_construidos': 140,
'num_baños': 2,
'num_habitaciones': 3,
'num_estacionamientos': 1,
'direccion': 'Avenida Siempre Viva 742',
'precio': 250000000,
'precio_ufs': 9000.75 }

inmueble = Inmueble.objects.create(
nombre='Casa en Santiago',
descripcion='Una hermosa casa en Santiago.',
m2_construidos=100.00,
m2_terreno=200.00,
numero_estacionamientos=2,
numero_baños=2,
numero_habitaciones=3,
direccion='Calle Falsa 123',
tipo_inmueble='casa',
precio_mensual=500000.00,
estado='disponible',
comuna=comuna,
arrendador=arrendador
)

# Crear una Solicitud:

from .models import Solicitud, Inmueble
from django.contrib.auth.models import User

inmueble = Inmueble.objects.get(id=1)
arrendatario = User.objects.get(username='pedro')

solicitud = Solicitud.objects.create(
inmueble=inmueble,
arrendatario=arrendatario,
estado='pendiente'
)

2. # Leer (Read) CONSULTAS POR SHELL

# Obtener todos los UserProfile:

user_profiles = UserProfile.objects.all()

# Obtener una Región específica:

region = Region.objects.get(cod='01')

# Filtrar Comunas por Región:

comunas = Comuna.objects.filter(region\_\_cod='01')

# Obtener un Inmueble específico:

inmueble = Inmueble.objects.get(id=1)

# Filtrar Solicitudes por estado:

solicitudes_pendientes = Solicitud.objects.filter(estado='pendiente')

3. Actualizar (Update)

# Actualizar un UserProfile:

user_profile = UserProfile.objects.get(id=1)
user_profile.direccion = 'Calle Verdadera 456'
user_profile.save()

# Actualizar una Región:

region = Region.objects.get(cod='01')
region.nombre = 'Nueva Región Metropolitana'
region.save()

# Actualizar un Inmueble:

inmueble = Inmueble.objects.get(id=1)
inmueble.precio_mensual = 600000.00
inmueble.save()

# Actualizar una Solicitud:

solicitud = Solicitud.objects.get(id=1)
solicitud.estado = 'aprobada'
solicitud.save()

4. Eliminar (Delete)

# Eliminar un UserProfile:

user_profile = UserProfile.objects.get(id=1)
user_profile.delete()

# Eliminar una Región:

region = Region.objects.get(cod='01')
region.delete()

# Eliminar una Comuna:

comuna = Comuna.objects.get(cod='01001')
comuna.delete()

# Eliminar un Inmueble:

inmueble = Inmueble.objects.get(id=1)
inmueble.delete()

# Eliminar una Solicitud:

solicitud = Solicitud.objects.get(id=1)
solicitud.delete()

m7_python > → services.py > actualizar_descrp_inmueble from m7_python.models import Inmuebles
def get_all_inmuebles():
Inm = Inmuebles.objects.all()
return Inm
def insertar_inmueble(data):
id_user = data[0]
id_tipo_inmueble = data[1] id_comuna = data[2]
id_region = data[3]
12
nombre_inmueble
=
data[4]
13
descripcion = data[5]
14
m2_construido
=
data[6]
15
numero_banos =
data[7]
16
17
numero_hab = data[8] direccion = data[9]
inm =
Inmuebles (
id_user = id_user,
id_tipo_inmueble
=
id_tipo_inmueble,
id_comuna = id_comuna,
id_region
=
id_region,
nombre_inmueble = nombre_inmueble,
descripcion
=
descripcion,
m2_construido = m2_construido,
numero_banos = numero_banos,
numero_hab = numero_hab,
direccion = direccion)
inm.save()

data = {
'id_user': 1,
'tipo_inmueble': 'Apartamento',
'comuna_cod': '002',
'nombre': 'Apartamento Moderno',
'descripcion': 'Un apartamento en pleno centro de la ciudad',
'm2_totales': 150,
'm2_construidos': 140,
'num_baños': 2,
'num_habitaciones': 3,
'num_estacionamientos': 1,
'direccion': 'Avenida Siempre Viva 742',
'precio': 250000000,
'precio_ufs': 9000.75
}
