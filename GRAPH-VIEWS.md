
# "/login_register" HOME
```

    INICIAR SESIÓN (Form)          REGISTRARME (Form)

   |------------------|             |------------------|
   |                  |             |                  |
   |                  |             |                  |
   |                  |             |                  |
   |------------------|             |------------------|            
     --> "/dashboard"                 --> "/register_tipo_usuario"
```

# "/register_tipo_usuario"

```
   |------------------|             
   |                  |            
   |  tipo_usuario    | --> 'arrendador'  || 'arrendatario'          
   |                  |             
   |------------------|   

```




# "/"  - "dashboard"

```py
def dashboard_view():
    if tipo_usuario == 'arrendador':
        redirect "/dashboard_arrendador"
    else:
        redirect "/dashboard_arrendatario"
```

# "/dashboard_arrendador"

```html
NavBar  Perfil

Lista de sus inmuebles publicados 
Crea un Inmueble (nueva publicación)
Editar un inmueble
Eliminar un inmueble (baneo sirve)

Marcar disponibilidad
Aceptar o rechazar solicitud

Footer
```


# "/dashboard_arrendatario"

```html
NavBar  Perfil

Lista de todos los inmuebles

La única acción del arrendatario es tocar un Inmueble y hacer solicitud


Footer
```


## ARRENDADOR

- Vistas
    - dashboard_arrendador - (index || home del arrendador)
        - LISTA de los INMUEBLES del arrendador
    - perfil_arrendador
    - form_crear_inmueble 
    - form_editar_inmueble
    - lista_solicitudes
    - detail_inmueble (extra)

- INMUEBLE
    - Botón para EDITAR
    - Botón para ELIMINAR
    - Botón para VER SOLICITUDES 
    - Botón para cambiar DISPONIBILIDAD

## ARRENDATARIO 
- Vistas
    - dashboard_arrendatario - (index || home del arrendatario)
        - LISTA de TODOS los INMUEBLES
    - perfil_arrendatario
    - Formulario de Solicitud
