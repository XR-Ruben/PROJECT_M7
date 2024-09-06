import os
import django
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import project_M7
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_m7.settings")
django.setup()

from m7_python.models import Inmueble, Region, Comuna 
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE","project_M7.settings")
django.setup()


#TODO_ Ejemplos SIMPLES:
def get_list_inmuebles_sql():
    select = """
        SELECT * FROM m7_python_inmueble
        """
    inmuebles = Inmueble.objects.raw(select)
    # inmuebles = Inmueble.objects.all()     <- ORM
    index=1
    print("LISTA INMUEBLES")
    for l in inmuebles:
        print(f"{index}__ {l.nombre}, {l.descripcion}")
        index += 1
    with open("m7_python/outputs/data.txt", "a") as file:
        for l in inmuebles:
            # print(f" {l.nombre}, {l.descripcion}")
            file.write(f" {l.nombre}, {l.descripcion}\n")
                
    return

def listado_inmuebles_comuna_orm(comuna):
    # inmuebles = Inmueble.objects.all()
    # comuna__nombre__icontains
    # Guardar la data en nuestro .txt con nuestro OPEN de python
    inmuebles = Inmueble.objects.filter(comuna__nombre__icontains=comuna)
    
    # filtros = {
    #         'comuna__nombre__icontains': comuna
    # }
    # if descr:
    #     filtros['descripcion__icontains'] = descr
        
    # inmuebles = Inmueble.objects.filter(**filtros)
    
    with open("m7_python/outputs/data.txt", "a") as file:
        file.write(f" __ listado_inmuebles_comuna_orm __\n")
        for l in inmuebles:
            file.write(f" {l.nombre}, {l.descripcion} - comuna: {l.comuna.nombre}\n")
        
    print(f"ïnmuebles")
    return

def listado_inmuebles_comuna_sql(comuna):
    #* posiblemente deben implementar el JOIN Inmueble y Comuna
    # ILIKE
    select = """
    SELECT A.id, A.nombre AS nombre_inmueble, A.descripcion
    FROM m7_python_inmueble A
    INNER JOIN m7_python_comuna C ON A.comuna_id = C.cod
    WHERE C.nombre ILIKE %s
    """
    inmuebles = Inmueble.objects.raw(select, [f"%{comuna}%"])
    # Guardar la data en nuestro .txt con nuestro OPEN de python
    with open("m7_python/outputs/data.txt", "a") as file:
        file.write(f'\n __ listado_inmuebles_comuna_sql __\n')
        for l in inmuebles:
            file.write(f"{l.nombre}, {l.descripcion} - comuna: {l.comuna.nombre}\n")
    return    
    

def listado_inmuebles_region_orm(region):
    # inmuebles = Inmueble.objects.all()
    inmuebles = Inmueble.objects.filter(comuna__region__nombre__icontains=region)
    
    with open("m7_python/outputs/data.txt", "a") as file:
        file.write(f" __ listado_inmuebles_region_orm __\n")
        for l in inmuebles:
            file.write(f" {l.nombre}, {l.descripcion} - region: {l.comuna.region.nombre}\n")
    print(f"inmuebles")
        
   
    return
    
    
    
# def listado_inmuebles_region_sql(comuna):
#     #* posiblemente deben implementar el JOIN Inmueble y Comuna
#     # ILIKE
#     select = """
#     SELECT A.id, A.nombre AS nombre_inmueble, A.descripcion
#     FROM m7_python_inmueble A
#     INNER JOIN m7_python_comuna_region C ON A.region_id = C.cod
#     WHERE C.nombre ILIKE %s
#     """
#     inmuebles = Inmueble.objects.raw(select, [f"%{region}%"])
#     # Guardar la data en nuestro .txt con nuestro OPEN de python
#     with open("m7_python/outputs/data.txt", "a") as file:
#         file.write(f'\n __ listado_inmuebles_region_sql __\n')
#         for l in inmuebles:
#             file.write(f"{l.nombre}, {l.descripcion} - region: {l.comuna.region.nombre}\n")
#     return    

# Ejecución de funciones de ejemplo
if __name__ == "__main__":
    #TODO_ Ejemplos SIMPLES:
    # get_list_inmuebles_sql() 
    listado_inmuebles_comuna_orm("que")
    listado_inmuebles_comuna_sql("pu")
    listado_inmuebles_region_orm("De Valparaiso")
    # listado_inmuebles_region_sql("Tarapaca")
    
    

    
# Archivo de testing
#! -> se ejecuta con --> python m7_python/temp.py <-- corre con    