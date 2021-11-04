class Persona:
    def __init__(self, nombre, edad, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
           
    def nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'

class Alumno(Persona): #se indica en el parentesis de quien hereda
    def __init__(self, nombre, apellidos, edad, carrera, calificaciones):
        super().__init__(nombre, edad, apellidos)
       
        self.carrera = carrera
        self.calificaciones = calificaciones
        
    def aprobado(self):
        if self.promedio() >= 70:
            return True
        else: 
            return False
    
    def promedio(self):
        sum= 0
        for calificacion in self.calificaciones:
            sum += calificacion
        return sum / len(self.calificaciones)
    
  
alumno_1 = Alumno('Wilco', 'Den', 45, 'Ingeniería Comunicaciones', [67, 87,90])
alumno_2 = Alumno('Jazmin', 'Mayo', 56, 'Psicología', [45, 99, 100])
alumno_3 = Alumno('Enriqueta', 'Perez', 34, 'Comunicaciones', [99, 85, 83])

alumnos = [alumno_1, alumno_2, alumno_3]

for alumno in alumnos:
    print(alumno.nombre_completo())
    print(alumno.promedio())
    print(alumno.calificaciones)
    print(alumno.carrera)
    print(alumno.aprobado())

