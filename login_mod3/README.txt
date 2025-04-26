Asignación: Autenticación Básica de Usuarios con Flask-Login

Descripción:
Este proyecto implementa un sistema básico de autenticación de usuarios usando Flask y Flask-Login. Permite a los usuarios registrarse, iniciar sesión y acceder a páginas protegidas que requieren autenticación. Las contraseñas se almacenan de forma segura utilizando hashing.

Requisitos:
- Python
- Flask
- Flask-Login
- Werkzeug (para el hashing de contraseñas)

Instalación:
1. Instalar los paquetes necesarios:
   pip install flask flask-login

Cómo Ejecutar:
1. Asegúrate de estar en la carpeta del proyecto.
2. Ejecuta la aplicación Flask:
   python app.py
3. Abre tu navegador web y entra a:
   http://localhost:5000/login
   o
   http://localhost:5000/register

Estructura del Proyecto:
- app.py (Servidor principal de Flask con rutas para login, logout y página protegida)
- templates/
    - login.html
    - register.html
    - protected.html

Notas:
- Solo los usuarios registrados pueden acceder a la página protegida.
- Las contraseñas están hasheadas para mayor seguridad.
- La gestión de sesiones se maneja a través de Flask-Login.

Autor:
Josiah Colon
