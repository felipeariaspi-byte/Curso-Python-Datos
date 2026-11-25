#diccionarios

televisores = {
    "marca": "Samsung",
    "precio": 5400000,
    "pulgadas": 50,
    "color": "negro",
    "resolucion": "4k"
}

print(televisores["marca"])
print(televisores["precio"])
print(televisores["pulgadas"])
print(televisores["color"])
print(televisores["resolucion"])

#consultar informacion get
#corchetes

print(televisores["precio"])

#parentesis

print(televisores.get("disponible"))
print(televisores.get("precio"))
print(televisores.get("pulgadas"))

#agregar informacion

televisores["disponible"]=False
print(televisores)

#modificar informacion

televisores["precio"] = 6000000
print(televisores)

#eliminar informacion

del televisores["disponible"]
print(televisores)

#consultar grupo de datos

print(televisores.keys())
print(televisores.values())
print(televisores.items())

#coleccion de datos

electrodomesticos_cocina = [
    {
        "producto": "microondas",
        "marca": "LG",
        "color": "plateado",
        "litros": 22,
        "disponible": True
},
{
    "producto": "sanduchera",
            "marca": "oster",
            "color": "negro",
            "disponible": True

}
]

print(electrodomesticos_cocina[0]["marca"])
print(electrodomesticos_cocina[1]["marca"])

#practica

producto_1 = {"codigo": "01", "nombre": "teclado", "precio": 75}
producto_2 = {"codigo": "02", "nombre": "ventilador", "precio": 120}
producto_3 = {"codigo": "03", "nombre": "audifonos", "precio": 250}

inventario = [producto_1, producto_2, producto_3]

print("Primer producto:", inventario[0]["nombre"])
print("precio del segundo:", inventario[1]["precio"])
print("Tercer prodcuto:", inventario[2]["nombre"] )

inventario[0]["precio"] = 87
print("Nuevo precio:", inventario[0]["precio"])

#conjuntos

canales = {"instagram", "facebook", "tiktok"}

print(canales)

#agregar un canal

canales.add("linkedin")

print(canales)

#comprobar si un elemento esta en el conjunto

print("instagram" in canales)

print("youtube" in canales)

#unir conjuntos

campania_a = {"instagram", "facebook", "tiktok"}
campania_b = {"linkedin", "youtube", "tiktok"}

campania_c = campania_a | campania_b
print(campania_c)

campania_d = campania_a & campania_b
print(campania_d)

campania_e = campania_a - campania_b
print(campania_e)

#actividad

producto1 = {
    "Articulo": "Portatil",
    "precio": 350.00,
    "cantidad": 5,
    "categoria": "Tecnologia"
}

producto2 = {
    "Articulo": "Mouse",
    "precio": 50.00,
    "cantidad": 10,
    "categoria": "Accesorios"}

productos = [producto1, producto2]

print(productos)

print("Buscar:" , productos[0]["Articulo"])
productos[0]["cantidad"] = 3
print("cantidad disponible:", productos[0]["cantidad"])

categorias = set()
for producto in productos:
    categorias.add(producto["categoria"])

print("\n-- CATEGORIAS EN STOCK --")
print(categorias)