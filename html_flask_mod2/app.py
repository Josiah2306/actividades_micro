from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

usuarios = []
productos = [
    {"nombre": "Camiseta", "precio": 20.99},
    {"nombre": "Pantalón", "precio": 35.50},
    {"nombre": "Zapatos", "precio": 50.75}
]

@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "app": "Sistema de Gestión",
        "version": "1.0",
        "estado": "activo"
    })

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Falta el nombre o el correo"}), 400
    
    nuevo_usuario = {
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)  

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios_page')
def usuarios_page():
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/productos_page')
def productos_page():
    return render_template('productos.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
