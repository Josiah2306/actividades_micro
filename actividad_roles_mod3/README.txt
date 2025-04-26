Proyecto de Autenticación y Autorización con Flask

Descripción
Esta aplicación Flask implementa:
- Autenticación de usuarios usando Flask-Login.
- Autorización basada en roles usando Flask-Principal.
- Protección de rutas según el rol del usuario (admin o user).
- Páginas HTML básicas usando Jinja2 (login, dashboard, admin, user, error 403).

Instalación
1. Clona el proyecto.
2. Instala los módulos necesarios:

pip install Flask Flask-Login Flask-Principal

3. Ejecuta el servidor:

python app.py

4. Accede a la aplicación desde tu navegador en:

http://127.0.0.1:5000/

Flujo de autenticación
1. El usuario entra en la URL /.
2. Se muestra un mensaje para iniciar sesión usando /login/juan o /login/maria.
3. Después del login, el usuario es redirigido al Dashboard (/dashboard).
4. Dependiendo de su rol:
   - Usuarios "admin" pueden acceder a /admin.
   - Usuarios "user" pueden acceder a /user.
5. Si un usuario intenta entrar a una ruta no autorizada, verá la página de error 403.

Datos de prueba
- Usuario Admin:
  - Username: juan
  - Rol: admin

- Usuario Normal:
  - Username: maria
  - Rol: user

Autor
Josiah Colon
