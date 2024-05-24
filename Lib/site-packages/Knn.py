import matplotlib.pyplot as plt

# Datos de entrenamiento
peso = [60, 45, 60, 62, 70, 75, 80, 50, 55]
altura = [160, 155, 168, 165, 170, 160, 190, 155, 160]
talla = ['M', 'S', 'M', 'M', 'L', 'L', 'L', 'S', 'S']

datos = list(zip(peso, altura, talla))

def distancia_euclidiana(punto1, punto2):
    return ((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2) ** 0.5

def k_vecinos_mas_cercanos(data, punto, k):
    distancias = []
    for dato in data:
        dist = distancia_euclidiana(punto, dato)
        distancias.append((dato, dist))
    distancias.sort(key=lambda x: x[1])
    vecinos = [distancias[i][0] for i in range(k)]
    return vecinos

def clasificar(vecinos):
    votos = {}
    for vecino in vecinos:
        etiqueta = vecino[2]
        if etiqueta in votos:
            votos[etiqueta] += 1
        else:
            votos[etiqueta] = 1
    votos_ordenados = sorted(votos.items(), key=lambda x: x[1], reverse=True)
    return votos_ordenados[0][0]

def knn_clasificacion(data, punto, k):
    vecinos = k_vecinos_mas_cercanos(data, punto, k)
    return clasificar(vecinos)

def obtener_nuevo_punto(peso, altura):
    return (peso, altura)

# Ejemplo de clasificación
nuevo_punto = obtener_nuevo_punto(62,173)
k = 3  # Número de vecinos
resultado = knn_clasificacion(datos, nuevo_punto, k)

# Graficar datos de entrenamiento
for dato in datos:
    if dato[2] == 'M':
        plt.scatter(dato[0], dato[1], color='blue', label='M')
    elif dato[2] == 'S':
        plt.scatter(dato[0], dato[1], color='green', label='S')
    else:
        plt.scatter(dato[0], dato[1], color='red', label='L')

# Graficar nuevo punto
plt.scatter(nuevo_punto[0], nuevo_punto[1], color='pink', label='Nuevo punto')

# Encontrar k vecinos más cercanos
vecinos = k_vecinos_mas_cercanos(datos, nuevo_punto, k)
for vecino in vecinos:
    plt.scatter(vecino[0], vecino[1], color='orange', label='Vecino')

plt.xlabel('Peso')
plt.ylabel('Altura')
plt.title('Clasificación con k-NN')
plt.legend()
plt.grid(True)
plt.show()

print(f"La talla seleccionada es: {resultado}")
