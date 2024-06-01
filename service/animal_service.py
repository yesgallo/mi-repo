
from abc import ABC, abstractmethod

class AnimalService(ABC):
    @abstractmethod
    def obtener_sonido(self):
        pass

    @abstractmethod
    def alimentar(self, comida):
        pass
