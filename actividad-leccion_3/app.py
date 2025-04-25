from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({

        "app": "Sistema del Gestion",
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

if __name__ == '__main__':
    app.run(debug=True)