
from .animal_service import AnimalService

class ComidaIncorrectaException(Exception):
    pass

class LeonService(AnimalService):
    def obtener_sonido(self):
        return "Rugido"

    def alimentar(self, comida):
        if comida != "carne":
            raise ComidaIncorrectaException("El león solo come carne.")
        return "El león está comiendo carne."
