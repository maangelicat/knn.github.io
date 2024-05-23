from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_talla', methods=['POST'])
def calcular_talla():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']
    talla_estimada = knn_clasificacion(datos, [peso, altura], 3)
    return jsonify({'talla': talla_estimada})

if __name__ == '__main__':
    app.run(debug=True)
