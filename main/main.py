
from controller.animal_controller import AnimalController

def main():
    controlador = AnimalController()
    
    print(controlador.obtener_sonido_leon())
    print(controlador.obtener_sonido_perro())

    print(controlador.alimentar_leon("carne"))
    print(controlador.alimentar_leon("alimento balanceado"))
    
    print(controlador.alimentar_perro("alimento balanceado"))
    print(controlador.alimentar_perro("carne"))

if __name__ == "__main__":
    main()
