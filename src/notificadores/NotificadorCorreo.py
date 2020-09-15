from src.InterfaceNotificador import InterfaceNotificador
import smtplib

class NotificadorCorreo(InterfaceNotificador):

    def __init__(self):
        super().__init__()
    
    def enviar(self, mensaje):

        sender = "Private Person <from@smtp.mailtrap.io>"
        receiver = "A Test User <to@smtp.mailtrap.io>"

        message = f"""\
        Subject: Hola!
        To: {receiver}
        From: {sender}

        {mensaje}."""
        try:
            server = smtplib.SMTP("smtp.mailtrap.io", 25) 
            server.login("79018c65b97ac2", "c1a1d855454362")
            server.sendmail(sender, receiver, message)
            print("Correo enviado")
        except: 
            print("Error: el mensaje no pudo enviarse")

        return 'mensaje enviado de correo'