
from service.leon_service import LeonService, ComidaIncorrectaException
from service.perro_service import PerroService

class AnimalController:
    def __init__(self):
        self.leon_service = LeonService()
        self.perro_service = PerroService()

    def obtener_sonido_leon(self):
        return self.leon_service.obtener_sonido()

    def obtener_sonido_perro(self):
        return self.perro_service.obtener_sonido()

    def alimentar_leon(self, comida):
        try:
            return self.leon_service.alimentar(comida)
        except ComidaIncorrectaException as e:
            return str(e)

    def alimentar_perro(self, comida):
        try:
            return self.perro_service.alimentar(comida)
        except ValueError as e:
            return str(e)
