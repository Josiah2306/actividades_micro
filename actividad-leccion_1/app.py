from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/info', methods=['GET'])

def get_info():
    return jsonify({

        "app": "Capstone Demo App",
        "version": "1.0",
        "status": "running"

    })

@app.route('/mensaje', methods=['POST'])

def post_mensaje():

    data = request.get_json()
    mensaje  = data.get('mensaje', 'No se recibio ningun mensaje.')

    return jsonify({

        "respuesta": f"recibio: {mensaje}"

    })

if __name__ == '__main__':

    app.run(debug=True)