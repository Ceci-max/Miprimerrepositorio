class Alumno: 
    def __init__(self,nombre):
        self.nom = nombre
    def saludar(self):
         """Imprime un saludo en pantalla."""
         print(f"¡Hola, {self.nom}!")
n=input ("Ingresa tu nombre")
x=Alumno(n)
x.saludar()

