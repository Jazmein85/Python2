class Animal:
    def __init__(self, nombre, especie, sonido= ''):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def info(self):
        print(f'Nombre: {self.nombre} - Especie: {self.especie} - Sonido {self.sonido}')
    
    def grito(self):
        if self.sonido == '':
            print('El animal no hace ningun ruido')
        else:
            print('El animal hace', self.sonido)

class Pez(Animal): #es una extensión de la clase Animal
    def nadar(self):
        print(f'El animal {self.nombre} está nadando')

perro = Animal('perro', 'canino', 'guau')
gato = Animal('gato', 'felino', 'miau')
pez_globo = Pez('pez', 'fish', None) #se toma desde la extensión de la clase Animal, es decir, Pez


animales = [perro, gato, pez_globo]
for animal in animales:
    animal.info()
    animal.grito()

pez_globo.nadar()



