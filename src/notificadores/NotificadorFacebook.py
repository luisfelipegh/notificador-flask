from src.InterfaceNotificador import InterfaceNotificador

class NotificadorFacebook(InterfaceNotificador):

    def __init__(self):
        pass

    def enviar(self, mensaje):
        return 'mensaje enviado de Facebook'