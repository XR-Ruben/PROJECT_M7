from django.contrib.auth.models import User
from .models import UserProfile, Region, Comuna, Inmueble, Solicitud

# Crear un objeto con el modelo:

def crear_usuario(username:str, first_name:str, last_name:str, email:str, password:str) -> bool:
    user = User.objects.create_user(
        username,
        email,
        password,
        first_name=first_name,
        last_name=last_name
        )
    UserProfile.objects.create(
        tipo='arrendatario', 
        user=user
        )
    return True

# def create_user(new_user):
#     user = User.objects.create_user(
#         username=new_user['username'],
#         email=new_user['email'],
#         first_name=new_user['first_name'],
#         last_name=new_user['last_name'],
#         password=new_user['password']
#     )
#     return user

# Crear una Región:
def create_region(cod, nombre): 
    region = Region(cod=cod, nombre=nombre)
    region.save()
    return region

# # Crear una Comuna:
def create_comuna(cod, nombre, region_cod):
    region = Region.objects.get(cod=region_cod)
    comuna = Comuna.objects.create(cod=cod, nombre=nombre, region= region)
    return comuna

# # # Crear un Inmueble:
def insertar_inmueble(data):
    """
    Inserta un nuevo inmueble en la base de datos.
    Parámetros:
        data (dict): Un diccionario con la información del inmueble a insertar.
            {
                'id_user': int,
                'tipo_inmueble': str,
                'comuna_cod': str,
                'nombre': str,
                'descripcion': str,
                'm2_totales': int,
                'm2_construidos': int,
                'num_baños': int,
                'num_habitaciones': int,
                'num_estacionamientos': int,
                'direccion': str,
                'precio': int,
                'precio_ufs': float
            }
    """
    # Obtener el usuario (arrendador) por ID
    arrendador = User.objects.get(id=data['id_user'])
    # Obtener la comuna por código (cod)
    comuna = Comuna.objects.get(cod=data['comuna_cod'])
    
     # Crear un nuevo Inmueble usando los datos proporcionados
    inmueble = Inmueble(
        arrendador=arrendador,
        tipo_inmueble=data['tipo_inmueble'],
        comuna=comuna,
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        m2_construidos=data['m2_construidos'],
        m2_totales=data['m2_totales'],
        num_baños=data['num_baños'],
        num_habitaciones=data['num_habitaciones'],
        num_estacionamientos=data.get('num_estacionamientos', 0),
        direccion=data['direccion'],
        precio=data.get('precio', None),
        precio_ufs=data.get('precio_ufs', None)
        # disponible al no pasar por defecto es True
    )
    inmueble.save()
    return inmueble

def get_all_inmuebles():
    inmuebles = Inmueble.objects.all()
    return inmuebles


def actualizar_disponibilidad_inmueble(id_inmueble, disponible):
    """
    Actualiza la disponibilidad de un inmueble existente.
    Parámetros:
        id_inmueble (int): ID del inmueble a actualizar.
        disponible (bool): Nueva disponibilidad para el inmueble.
    Retorna:
        dict: Resultado de la operación con un mensaje de éxito o error.
    """
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)  # Buscar el inmueble por ID
        # Actualizar la disponibilidad
        inmueble.disponible = disponible
        # inmueble.direccion = direccion
        # inmueble.descripcion = descripcion
        
        inmueble.save()  # Guardar los cambios
        return {
            "success": True,
            "message": "Disponibilidad actualizada con éxito"
        }
    except Inmueble.DoesNotExist:
        return {
            "success": False,
            "message": "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al actualizar la disponibilidad del inmueble: {str(e)}"
        }

def eliminar_inmueble(id_inmueble):
    """
    Elimina un inmueble de la base de datos si existe.
    Parámetros:
        id_inmueble (int): ID del inmueble a eliminar.
    Retorna:
        dict: Resultado de la operación con un mensaje de éxito o error.
    """
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)  # Buscar el inmueble por ID
        # Eliminar el inmueble
        inmueble.delete()
        return {
            "success": True,
            "message": "Inmueble eliminado con éxito"
        }
    except Inmueble.DoesNotExist:
        return {
            "success": False,
            "message": "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al eliminar el inmueble: {str(e)}"
        }
        
        

def crear_usuario(username:str, first_name:str, last_name:str, email:str, password:str) -> bool:
    user = User.objects.create_user(
        username,
        email,
        password,
        first_name=first_name,
        last_name=last_name
        )
    UserProfile.objects.create(
        tipo='cliente', 
        user=user
        )
    return True
        

# # Crear una Solicitud:

# inmueble = Inmueble.objects.get(id=1)
# arrendatario = User.objects.get(username='pedro')

# solicitud = Solicitud.objects.create(
# inmueble=inmueble,
# arrendatario=arrendatario,
# estado='pendiente'
# )

# nuevo_inmueble = Inmueble(
#     nombre="Casa en el centro",
#     descripcion="Hermosa casa de 3 habitaciones en el centro de la ciudad.",
#     m2_construidos=120.50,
#     m2_terreno=150.00,
#     numero_estacionamientos=2,
#     numero_baños=2,
#     numero_habitaciones=3,
#     direccion="Calle Principal 123",
#     id_comuna=Comuna.objects.get(id_comuna=1),
#     id_region=Region.objects.get(id_region=1),
#     tipo_inmueble="Casa",
#     precio_mensual=750.00,
#     estado="Disponible",
#     id_user=User.objects.get(id_user=1)
# )
# nuevo_inmueble.save()


# # Enlistar desde el modelo de datos:

# inmuebles = Inmueble.objects.all()
# for inmueble in inmuebles:
#     print(inmueble.nombre, inmueble.precio_mensual)


# # Actualizar un registro en el modelo de datos:

# inmueble = Inmueble.objects.get(id_inmueble=1)
# inmueble.precio_mensual = 800.00
# inmueble.save()


# # Borrar un registro del modelo de datos:

# inmueble = Inmueble.objects.get(id_inmueble=1)
# inmueble.delete()