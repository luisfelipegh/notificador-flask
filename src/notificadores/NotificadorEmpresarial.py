from src.InterfaceNotificador import InterfaceNotificador

class NotificadorEmpresarial(InterfaceNotificador):

    def __init__(self):
        super().__init__()
    
    def enviar(self, mensaje):
        return 'mensaje enviado Empresarial'