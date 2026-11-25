#sesion 3
# tipos de datos

# enteros (int)

edad =25
cantidad = 0
temperatura = -50

# flotantes (float)
precio = 10.5
pi = 3.1416
peso = 25.2
print(edad, cantidad,temperatura, precio, pi, peso)

# booleanos (bool)
requiere_inscripcion = True
esta_lluvioso = False
print(requiere_inscripcion, esta_lluvioso)

print(type(edad))
print(type(precio))
print(type(requiere_inscripcion))
print(type(pi))

#registro de ventas

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad de productos vendidos: "))
precio = float(input("Ingrese el precio unitario del producto: "))

total = cantidad * precio

print("producto:", producto)
print("total:", total)
