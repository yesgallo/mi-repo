
from .animal_service import AnimalService

class PerroService(AnimalService):
    def obtener_sonido(self):
        return "Ladrido"

    def alimentar(self, comida):
        if comida != "alimento balanceado":
            raise ValueError("El perro solo come alimento balanceado.")
        return "El perro está comiendo alimento balanceado."
