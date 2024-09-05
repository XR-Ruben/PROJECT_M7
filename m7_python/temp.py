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


# Ejecución de funciones de ejemplo
if __name__ == "__main__":
    #TODO_ Ejemplos SIMPLES:
    get_list_inmuebles_sql()
    
    
# Archivo de testing
#! -> se ejecuta con --> python m7_python/temp.py <-- corre con    