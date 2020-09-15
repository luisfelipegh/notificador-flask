from src.InterfaceNotificador import InterfaceNotificador

class NotificadorFacebook(InterfaceNotificador):

    def __init__(self):
        super().__init__()

    def enviar(self, mensaje):
        return 'mensaje enviado de Facebook'