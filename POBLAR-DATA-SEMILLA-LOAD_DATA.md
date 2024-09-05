
# LOAD-DATA (manage.py)

## Paso a paso para poblar la data a dicho proyecto

1. Haber realizado los MODELS
2. Haber realizado las MIGRATE 
3. Crear los .json necesarios
4. Ejecutar los comandos LOAD-DATA para cada .json segín el ORDEN correspondiente

Ejemplo:
```bash
python manage.py loaddata m7_python/data/users.json

python manage.py loaddata m7_python/data/regiones_comunas.json

python manage.py loaddata m7_python/data/inmuebles.json
```

```
COMANDO loaddata dentro del manage -> la APP nuestra m7_python y la carpeta data y el nameArchivo.json
python manage.py loaddata m7_python/data/users.json
```