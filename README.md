# TuPrimeraPagina-Cerpa
Proyecto final realizado en Django para el curso de Python.
Consiste en una aplicación web para la gestión de un Centro de Masajes, con sistema de servicios tipo blog, autenticación, perfiles y mensajería.

# Modelos creados
Cree los siguientes modelos:
- Cliente
- Servicio (refiere a tipo de masajes)
- Turno
- Page (Servicios tipo blog)
- Profile (perfil del usuario)
- Mensajería (threads y mensajes)

# Funcionalidades de la página web
En la página web se puede observar:
- Página de inicio
- Sección About / Acerca de mí
- Listado de servicios (Pages)
- Detalle de cada servicio
- Creación, edición y eliminación de servicios (solo usuarios logueados)
- Login / Signup / Logout
- Perfil de usuario
- Editar perfil (incluye datos del User + Profile)
- Cambio de contraseña desde perfil
- Mensajería (Inbox)

# Orden para probar la aplicacion
1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias
4. Ejecutar migraciones
5. Crear un superusuario
6. Ingresar al panel de administración
7. Probar las funcionalidades desde la web

# Pasos para ejecutar el proyecto
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

