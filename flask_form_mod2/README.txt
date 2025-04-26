Registro de Usuarios con Flask y WTForms

Descripción:
Este proyecto es un formulario de registro de usuarios utilizando Flask y Flask-WTF.
Permite a los usuarios ingresar su nombre, correo electrónico y contraseña, validando los datos antes de aceptar el registro.

Tecnologías Utilizadas:
- Python 3
- Flask
- Flask-WTF
- WTForms
- email_validator

Instrucciones para Ejecutar:
1. Instala las dependencias:
   pip install flask flask-wtf email_validator

2. Corre la aplicación:
   python app.py

3. Abre tu navegador y entra a:
   http://localhost:5000/register

Validaciones Implementadas:
- Nombre: Requerido, mínimo 3 caracteres.
- Correo Electrónico: Requerido, debe tener formato válido de correo.
- Contraseña: Requerida, mínimo 6 caracteres.

Estructura de Carpetas:
- /templates
    - register.html
    - success.html
- app.py

Capturas de Pantalla:
- Formulario de registro.
- Mensajes de error en validaciones.
- Página de éxito después de registrarse.

Autor:
Josiah Colon
