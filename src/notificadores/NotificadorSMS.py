from src.InterfaceNotificador import InterfaceNotificador

class NotificadorSMS(InterfaceNotificador):

    def __init__(self):
        super().__init__()
    
    def enviar(self, mensaje):
        return 'mensaje enviado de SMS'