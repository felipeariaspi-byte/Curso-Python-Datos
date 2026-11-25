# sesion 2
# ctrl+# para comentar una linea
#ctrl+/ para comentar varias lineas
#ctrl+c ctrl+k para comentar varias lineas
#ctrl+} para quitar comentario
#ctrl ctrl+/ para quitar el comentario de carias lineas

# Programa de bienvenida

print("Bienvenido al programa")

## Pregunta al usuario su nombre
nombre = input("por favor ingrese su nombre: " )
print("Su nombre es:", nombre )

#Concatenar el nombre con un mensaje
mensaje = "Hola " + nombre + ", bienvenido al programa"
print(mensaje)

#Variables
edad = input("por favor ingrese su edad: ")
print("Su edad es:", edad)

#expresiones y combinar valores
edad = int(edad)
edad = edad - 15
print("Su edad es:", edad)

#  Solicitar informacion al usuario
producto = input("Ingrese el nombre del producto: ")
cantidad = (input("Ingrese la cantidad de productos vendidos: "))
precio_unitario = (input("Ingrese el precio unitario del producto: "))

# Calcular el total de la venta
total = int(cantidad) * float(precio_unitario)

# Mostrar la informacion registrada
print("\n----- REGISTRO DE VENTA -----")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario:", precio_unitario)
print("Total:", total)

print("\nGracias por utilizar el programa de registro de ventas.")
