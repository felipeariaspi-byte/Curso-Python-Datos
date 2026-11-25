#sesion 7
#ciclo for

guias = ["G001", "G002", "G003", "G004", "G005"]

for memoria in guias:
    print("Revisando envio:", memoria)

#for+range

for consecutivo in range(2):
    print("revisando envio", guias[consecutivo])

for consecutivo in range(2,5):
     print("revisando envio", guias[consecutivo])

#contadores

contador = 0
for guia in guias:
    contador += 1
    print("revisando", guia)

print("total:", contador)

#acumuladores de km

distancias = [15, 22, 10, 18]
distancia_total = 0

for distancia in distancias:
    distancia_total += distancia
print("distancia total:", distancia_total)

#ciclo while
#intentos de entegas

envios = [
    {"estado": "entregado"},
    {"estado": "en ruta"},
    {"estado": "devuelto"},
    {"estado": "entregado"},
    {"estado": "devuelto"},
    {"estado": "entregado"}
]
entregados = 0
en_ruta = 0
devueltos = 0

for envio in envios:
    if envio["estado"] == "entregado":
        entregados += 1
    elif envio["estado"] == "en ruta":
        en_ruta += 1
    else:
        devueltos += 1

#MOSTRAR RESULTADOS
print("RESUMEN DE ENVIOS")
print("entregados:", entregados)
print("en ruta:", en_ruta)
print("devueltos:", devueltos)

#while

#intentos de entrega

guia = "G001"
intentos = 0
while intentos < 3 and entregados == False:
    intentod += 1
    entregados = True
if entregados:
    print("envio entregado:", guia)
else:
    print("envio no entregado:", guia)

guia = "G001"

intentos = 0
entregado = False

while intentos < 3 and entregado == False:
    intentos += 1

print("guia", guia)
print("intentos de entrega", intentos)

resultado = input("se entrego el paquete? (S/N):    ").lower()

if resultado == "s":
    entregado = True
else:
    entregado = False

if entregado:
    print("envio entregado")

else:
    print("envio devuelto")

#frecuencia de entregas en tiempo

tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0

for tiempo in tiempos:
    if 1 <= tiempo <=3:
        grupo_1_3 +=1
    elif 4 <= tiempo <=6:
        grupo_4_6 +=1
    elif 7 <= tiempo <=9:
        grupo_7_9 +=1
    elif 10 <= tiempo <=12:
        grupo_10_12 +=1

print ("Reporte tiempos de entrega")
print ("de 1 a 3 dias:", grupo_1_3, "entregas")
print ("de 4 a 6 dias:", grupo_4_6, "entregas")
print ("de 7 a 9 dias:", grupo_7_9, "entregas")
print ("de 10 a 12 dias:", grupo_10_12, "entregas")