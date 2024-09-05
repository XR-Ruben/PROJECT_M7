# UTF-8 - siempre FUNCIONAL

## SOLUCION seteo del sistema en WINDOWS

1. **Activar UTF-8 para Programas No Unicode (si no lo has hecho):**
   - Ve a **Panel de control** > **Reloj y región** > **Región**.
   - En la pestaña **Administrativo**, haz clic en **Cambiar configuración regional del sistema**.
   - Marca la opción **Beta: Usar Unicode UTF-8 para compatibilidad con el idioma mundial**.
   - Reinicia el sistema para aplicar los cambios.

2. **Verificar la Codificación en tu Archivo JSON:**
   - Asegúrate de que tu archivo JSON esté guardado con codificación UTF-8.
   - Puedes verificarlo abriendo el archivo en un editor de texto como Notepad++ o Visual Studio Code, y seleccionando **Guardar como**. En el cuadro de diálogo, asegúrate de que la codificación sea **UTF-8**.

3. **Verificar la Base de Datos PostgreSQL:**
   - Ya has creado una base de datos con UTF-8 y collation `Spanish_Argentina.utf8`.
   - Puedes ejecutar este comando para confirmar que todos los parámetros están configurados correctamente:

     ```sql
     SHOW SERVER_ENCODING;
     SHOW CLIENT_ENCODING;
     ```

   Ambos deberían devolver `UTF8`.

### **Ejecutar la Importación Nuevamente**

Intenta importar el archivo JSON usando `python manage.py loaddata` después de haber confirmado que tanto la configuración regional de Windows, la codificación del archivo JSON, y los ajustes de PostgreSQL son correctos.

---

## VERIFICAR UTF-8 en sistema

### **Abrir PowerShell**

1. Presiona `Windows + X` en tu teclado.
2. Selecciona **Windows PowerShell** o **Windows PowerShell (Administrador)** en el menú que aparece.

### **Ejecutar el Comando en PowerShell**

Una vez que tengas PowerShell abierto, ejecuta el siguiente comando:

```powershell
Get-WinSystemLocale
```

Este comando te mostrará la configuración regional actual del sistema, incluyendo el idioma y la codificación.

### **Si Necesitas Cambiar la Configuración a UTF-8**

1. Sigue las instrucciones anteriores para cambiar la configuración regional desde el Panel de Control, asegurándote de seleccionar una configuración que utilice UTF-8.
2. Si necesitas activar la opción de compatibilidad UTF-8, ve a **Región** > **Administrativo** y activa la opción **Beta: Usar Unicode UTF-8 para compatibilidad con el idioma mundial**.

Después de hacer estos cambios, es recomendable reiniciar el sistema para que se apliquen correctamente.

---
## COMANDO para reafirmar el LC_COLLATE y el LC_CTYPE en UTF8
```bash
CREATE DATABASE nueva_base WITH ENCODING 'UTF8' LC_COLLATE='Spanish_Argentina.utf8' LC_CTYPE='Spanish_Argentina.utf8' TEMPLATE template0 OWNER postgres;
```
**otro modo es:**

```bash
CREATE DATABASE nueva_base_utf8
WITH ENCODING 'UTF8'
LC_COLLATE='es_ES.UTF-8'
LC_CTYPE='es_ES.UTF-8'
TEMPLATE template0
OWNER postgres;
```

## VERIFICAR tipo de encoding de la db creada
```bash
SELECT datname, datcollate, datctype 
FROM pg_database 
WHERE datname = 'nueva_base';
```


temp.py 

config -> correr temp.py 
Consultas ORM -> objects (class Manager) -> métodos (filter, get, create, delete, update, all)
Consultas a puro SQL -> usando el RAW (método) dentro del objects (class Manager)

```py
nombre__contains
nombre__icontains
```

```sql
LIKE
ILIKE
```

```
1 Casa Baja 
2 Casa Media 
3 Casa Alta 

__contains LIKE    a  ->   las 3 -> [Casa Baja, Casa Media, Casa Alta]
__contains LIKE    Ba  ->   [Casa Baja]
__contains LIKE    ba  ->  []

__icontains ILIKE  
__contains LIKE    ba  ->   [Casa Baja]
```