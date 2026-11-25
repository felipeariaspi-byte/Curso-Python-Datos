# sesion 4
# consultar cadenas de texto

producto = "rinoceronte"
print(producto[0]) # r
print(producto[1]) # i
print(producto[2]) # n
print(producto[3]) # o
print(producto[4]) # c
print(producto[5]) # e
print(producto[6]) # r
print(producto[7]) # o
print(producto[8]) # n
print(producto[9]) # t
print(producto[10]) # e

#f strings construir mensajes con variables

print(f"el producto es: {producto}")

#posiciones positivas y negativas
print(producto[10]) # e
print(producto[-1]) # t

#extarer partes de una cadena de texto

print(producto[0:5]) # rinoc
print(producto[5:11]) # e ron
print(producto[1:]) # rnoet

#longitud cadena de texto

producto = " memoria ram 1tb"
longitud = len(producto)
print("la longitud de la cadena de texto es :", longitud)

#metodos de cadena de texto
#convertir a mayusculas

producto = "memoria ram 1tb"
print(producto.upper()) # MEMORIA RAM 1TB

#convertir a minusculas
print(producto.lower()) # memoria ram 1tb

#capitalizar la primera letra de la cadena de texto
print(producto.capitalize()) # Memoria ram 1tb

#reemplazar un caracter por otro
print(producto.replace("a", "u")) # memoria ram 2tb

#agergar una letra al final de texto
print(producto + " extra") # memoria ram 1tb extra

#eliminar espacios al inicio y al final de la cadena de texto
print(producto.strip()) # memoria ram 1tb

#limpiar base de datos
nombre = "  JORGE FELIPE ARIAS PINILLA    "
print(f" el nombre del cliente es: {nombre.strip().title()}") # el nombre del cliente es: Jorge felipe arias pinil

#ejercicio
nombres = ["  MARIA GOMEZ ",
          "  juan perez",
          " ANA LOPEZ  "
]

print("elprimer nombre es:", nombres[0]) 
print("el segundo nombre es:", nombres[1]) 
print("el tercer nombre es:", nombres[2]) 
print("limpiar el primer nombre:", nombres[0:1][0].strip().title())
print(f"los nombres de los clientes son: {nombres[0].strip().title()}, {nombres[1].strip().title()}, {nombres[2].strip().title()}")

#listas

listas = ["memoria ram 1tb","disco duro 2tb", "tarjeta grafica 8gb"]
print(listas)

#agregar un elemento al final de la lista
listas.append("procesador i7")
print(listas)

#agregar un elemento en una posicion especifica de la lista
listas.insert(1, "fuente de poder 600w")
print(listas)

#eliminar un elemento de la lista
listas.remove("disco duro 2tb")
print(listas)

#eliminar un elemento de la lista por su posicion
del listas[1]
print(listas)

#ordenar una lista
listas.sort()
print(listas)

#ordenar una lista en reversa
listas.sort(reverse=True)
print(listas)

#unir dos listas
listas2 = ["monitor 24 pulgadas", "teclado usb", "mouse inalambrico"]
listas3 = listas + listas2
print(listas3)

#convertir vadena de texto a lista
cadena = "memoria ram 1tb, disco duro 2tb, tarjeta grafica 8gb"
listas4 = cadena.split(", ")
print(listas4)

#contar elementos de una lista
print(len(listas4)) # 3

# ejercicio
ventas = ["portatil", "tablet", "smartphone", "cargador", "auriculares"]
print(ventas)
print(ventas[1]) # tablet
ventas[3] = "cargador rapido"
print(ventas) # ['portatil', 'tablet', 'smartphone', 'carg
ventas.insert(2, "smartwatch")
print(ventas) # ['portatil', 'tablet', 'smartwatch', 'smartphone', 'cargador rapido', 'auriculares']
ventas.remove("auriculares")
print(ventas) # ['portatil', 'tablet', 'smartwatch', 'smartphone', 'cargador rapido']
print(len(ventas)) # 5

#tuplas
unicaciones_geograficas = ("latitud", "longitud", "altitud")
print(unicaciones_geograficas)

coordenadas = (4.60971, -74.08175, 2600)
print(coordenadas)

estadistica_media = (10, 20, 30, 40, 50)
print(estadistica_media)