"""
AUTOR: PITAYA OLVERA CECILIA
FECHA: 23/08/24
Se piden 3 calificaciones de 1 al 100 asi como el nombre del lumno
Se promedia -> los alumnos que tengan calificacion menor a 70 se le imprime un emsaje de reprobado
Al finalizar el sistema se imprime el nombre y promedio del alumnocon mayor calificacion y el Alumno con menor clificacion

1. Abrir una libreria para 
Alumnos = []
Calificaciones = []
Donde se guardarna los datos que el usuario proporcionara
2. Con una variable para saber cuantos alumnos son preguntar al usuario
"¿Cuantos alumnos son?"
3.Pedir el al usuario el nombre del alumo
4. pedir la calificacion de cada alumno 
4.1 Si ingreso una calificacion erronea mandarle un abiso de que hizo mal al introducir los datos y pedirle nueva,mnte que ingrese los datos
(validado con "while")
5.Si hay alumnos reprobados  se calcula el promedio y lo imprime
6.Por ultimo se vuelven a checar las listas con el bocle for para checar asi ña calificacion mas alta y la mas baja para haci mostrarla en pantalla
"""
Alumnos = []
Calificaciones = []

CAN_Alumnos = int(input("¿Cuantos alumnos son?"))

for i in range (CAN_Alumnos):
    nombre = input("\n Ingresa el nombre del alumno",i+1)
    print("LA CALIFICACION DEVE SERR ENTRE 1 Y 100")
    calificacion= int (input("Ingrewsa la calificacion del alumno",1+i))

    while calificacion < 1 or calificacion > 100:
        print("La calificaciom deve ser entre 1 y 100")
        calificacion= int(input("Ingrese la calificacion de",i+1))

    Alumnos.append(nombre)
    calificacion.append(calificacion)


reprobados= [cal for cal in calificacion if cal <70]
if reprobados:
    PR_R = sum (reprobados)/len(reprobados)
    print("Reprobo con" ,PR_R)



for i in range(Alumnos):
    if calificacion[i] < 70:
        estado = "Reprobado"
    else:
        estado = "Aprobado"
    

