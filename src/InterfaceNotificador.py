from abc import ABC, abstractmethod

class InterfaceNotificador(ABC):

    @abstractmethod
    def enviar(self):
        pass