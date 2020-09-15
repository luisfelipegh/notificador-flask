from src.notificadores.NotificadorFacebook import NotificadorFacebook
from src.notificadores.NotificadorCorreo import NotificadorCorreo
from src.notificadores.NotificadorSMS import NotificadorSMS
from src.notificadores.NotificadorEmpresarial import NotificadorEmpresarial

class ControladorNotificador():

    def __init__(self):
        
        self.notificadores = {
            "Correo" : NotificadorCorreo,
            "Facebook" : NotificadorFacebook,
            "SMS" : NotificadorSMS,
            "Empresarial" : NotificadorEmpresarial
        }

    def crearNotificadores(self,ListaNotificaciones):
        
        notificadoresAEnviar = []
        
        for notificador in ListaNotificaciones:
            notificadoresAEnviar.append(self.notificadores[notificador]())

        return notificadoresAEnviar


        
