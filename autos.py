from _typeshed import Self


class Auto:
    # __init__ se corre al crear
    def __init__(self, modelo, gasolina):  # Metodos
        self.modelo = modelo  # Atributo
        self.gasolina = gasolina  # Atributo
        print('Auto', self.modelo, 'creado')

    def arrancar(self):  # Metodo
        if self.gasolina > 0:
            print('El auto', self.modelo, 'ha arrancado')
        else:
            print('El auto', self.modelo, 'no arranca')
    
    def recargar_gasolina(self):
        self.gasolina += 20
        print("Auto", self.modelo, "recargó 20 litros")

    def subir_pasajeros(self, *args):
        for arg in args:
            print("El pasajero", arg, "se ha subido al auto")

mi_auto = Auto('Tsuru', 0)
auto_vecino = Auto('Vocho', 0)
auto_otro = Auto('Jetta', 0)
auto_2 = Auto('BMW', 100)
auto_3 = Auto('Audi', 80)
auto_4 = Auto('GMC', 40)

autos = [mi_auto, auto_vecino, auto_otro, auto_2, auto_3, auto_4]

for auto in autos:
    auto.recargar_gasolina()
    auto.arrancar()

mi_auto.subir_pasajeros("Sergio", "Pablo", "Pedro")
print(mi_auto.__dict__)