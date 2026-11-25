
#control mantenimiento de la flota

#datos

flota = [
    {"codigo": "V-101", "kilometros": 320},
    {"codigo": "V-102", "kilometros": 780},
    {"codigo": "V-103", "kilometros": 1250},
    {"codigo": "V-104", "kilometros": 1680},
    {"codigo": "V-105", "kilometros": 450},
    {"codigo": "V-106", "kilometros": 920},
    {"codigo": "V-107", "kilometros": 1420},
    {"codigo": "V-108", "kilometros": 1850},
    {"codigo": "V-109", "kilometros": 610},
    {"codigo": "V-110", "kilometros": 1100},
    {"codigo": "V-111", "kilometros": 250},
    {"codigo": "V-112", "kilometros": 1550}
]

#contadores

uso_reciente = 0
seguimiento = 0
programar_revision = 0
prioridad_alta = 0

kilometraje_total = 0

#clasificar los vehiculos

print("Reporte de mantenimiento")

for vehiculo in flota:

    codigo = vehiculo["codigo"]
    kilometros = vehiculo["kilometros"]

    # Sumar de kilometros
    kilometraje_total += kilometros

    # Clasificar los vehiculos

    if kilometros >= 0 and kilometros <= 499:
        categoria = "Uso reciente"
        uso_reciente += 1

    elif kilometros >= 500 and kilometros <= 999:
        categoria = "Seguimiento"
        seguimiento += 1

    elif kilometros >= 1000 and kilometros <= 1499:
        categoria = "Programar revision"
        programar_revision += 1

    elif kilometros >= 1500 and kilometros <= 1999:
        categoria = "Prioridad alta"
        prioridad_alta += 1

    else:
        categoria = "Fuera de rango"

    # informacion de cada vehiculo

    print(f"Vehiculo: {codigo}")
    print(f"Kilometros: {kilometros}")
    print(f"Categoria: {categoria}")

#cantidad de vehiculos y promedio

cantidad_vehiculos = len(flota)

promedio = kilometraje_total / cantidad_vehiculos

#reporte final

print("\n Resumen de informacion ")

print(f"Vehiculos registrados: {cantidad_vehiculos}")

print(f"Uso reciente: {uso_reciente}")
print(f"Seguimiento: {seguimiento}")
print(f"Programar revision: {programar_revision}")
print(f"Prioridad alta: {prioridad_alta}")

print(f"Kilometraje total: {kilometraje_total} km")
print(f"Promedio de kilometraje: {promedio} km")

print("...")

#consultar vehiculo por codigo

continuar = "si"

while continuar == "si":

    print("\n Consultar por codigo ")

    codigo_buscar = input("Ingrese el codigo del vehiculo: ")

    encontrado = False

    #al desplegar la informacion

    for vehiculo in flota:

        if vehiculo["codigo"] == codigo_buscar.upper():

            kilometros = vehiculo["kilometros"]

            print(f"Codigo: {vehiculo['codigo']}")
            print(f"Kilometros: {kilometros}")

            # Identificar su categoria

            if kilometros >= 0 and kilometros <= 499:
                print("Categoria: Uso reciente")

            elif kilometros >= 500 and kilometros <= 999:
                print("Categoria: Seguimiento")

            elif kilometros >= 1000 and kilometros <= 1499:
                print("Categoria: Programar revision")

            elif kilometros >= 1500 and kilometros <= 1999:
                print("Categoria: Prioridad alta")

            else:
                print("Categoria: Fuera de rango")

            encontrado = True
            break

    if encontrado == False:
        print("Vehiculo no encontrado.")

    continuar = input(
        "\nDesea consultar otro vehiculo? (si/no): "
    ).lower()

