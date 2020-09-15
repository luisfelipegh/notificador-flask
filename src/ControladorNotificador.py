from .notificadores.NotificadorFacebook import NotificadorFacebook
from .notificadores.NotificadorCorreo import NotificadorCorreo
from .notificadores.NotificadorSMS import NotificadorSMS

class ControladorNotificador():

    def __init__(self):
        
        self.notificadores = {
            "Correo" : NotificadorCorreo,
            "Facebook" : NotificadorFacebook,
            "SMS" : NotificadorSMS
        }

    def crearNotificadores(self,ListaNotificaciones):
        
        notificadoresAEnviar = []
        
        for notificador in ListaNotificaciones:
            notificadoresAEnviar.append(self.notificadores[notificador]())

        return notificadoresAEnviar


        
