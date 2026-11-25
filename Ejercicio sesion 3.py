# Actividad

# variables
actividad = "Curso Python"
cupos = 25
duracion_horas = 15
requiere_inscripcion = False

actividad = input("nombre de la actividad ")
cupos = int(input("numero de cupos disponibles "))
duracion_horas = float(input("duracion de la actividad "))
requiere_inscripcion = bool(input("requiere inscripcion (True/False): "))


print("Actividad:", actividad)
print("Cupos disponibles:", cupos)
print("Duracion en horas:", duracion_horas)
print("Requiere inscripcion:", requiere_inscripcion)

# Tipos de datos
print(type(actividad))
print(type(cupos))
print(type(duracion_horas))
print(type(requiere_inscripcion))