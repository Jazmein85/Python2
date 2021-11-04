class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else: 
            return False
    def nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'
    
persona_1 = Persona('Wilco', 'Den', '40')
persona_2 = Persona('Jazmin', 'Mayo', '30')
persona_3 = Persona('Enriqueta', 'Perez', '40')

personas = [persona_1, persona_2, persona_3]

for persona in personas:
    print(persona.nombre_completo())
    print(persona.nombre)
