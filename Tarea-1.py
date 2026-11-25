archivo = input("ingrese titulo: ")
print(archivo)

area_comercial = "ventas_ocho_meses"
informacion_ventas = [95, 75, 85, 95, 92, 70, 95, 87]
print(informacion_ventas)

#total de ventas
total = sum(informacion_ventas)
print(f"Total {area_comercial}: {total}")

#media de ventas
media = total / len(informacion_ventas)
print("media:", media)

datos_ordenados = sorted(informacion_ventas)
print(informacion_ventas)

#mediana
datos_ordenados = sorted(informacion_ventas)
print(datos_ordenados)
mediana = (datos_ordenados[3] + datos_ordenados[4] / 2)
print("mediana:",mediana)

frecuencia_95 = informacion_ventas.count(95)
print("frecuencia del 95:", frecuencia_95)

#top_mas_vedndidos
top = ["tablet, laptop, smart watch, ps5, audifonos"]
print(top)

articulos ="tablet,laptop,smart watch,ps5,audifinos"
lista = articulos.split(",")
print(lista)
print(len(lista))

formas_de_pago = ("efectivo", "tarjeta", "llaves/nequi")
print(formas_de_pago)

nombre = "  felipe ARias  "
Encargado = nombre.strip().title()
print(Encargado)