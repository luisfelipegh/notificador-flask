from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
from src.ControladorNotificador import ControladorNotificador

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

@app.route('/', methods=['GET'])
def notificadores():
    return jsonify({
        'notificadores' : [
            'Correo',
            'Facebook',
            'SMS'
        ]
    }),200


@app.route('/enviar', methods=['POST'])
def notificar():
    body = request.get_json()

    controlador = ControladorNotificador()

    listaNotificadora = controlador.crearNotificadores(body['notificadores'])

    responseService = []
    for Noti in listaNotificadora:
        responseService.append(Noti.enviar(body['mensaje']))

    return jsonify({'responses' : responseService}),200


app.run()