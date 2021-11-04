class Pato:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def moverse(self):
        return (f'El pato {self.nombre} comienza a caminar')
    
    def grito(self):
        return (f'El pato {self.nombre} hace quack')
    

class Humano:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f'El humano {self.nombre}imita al pato y  se pone plumas')
    
    def moverse(self):
        return f'El humano {self.nombre} comienza a caminar como pato'
    
    def grito(self):
            return (f'El humano {self.nombre} hace quack')
    
    
    patos = [Pato('Donald'), Pato('Lucas')]
    
    for pato in patos:
        print(pato.grito())
        print(pato.moverse())

