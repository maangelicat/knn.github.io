from Knn import distancia_euclidiana, k_vecinos_mas_cercanos, clasificar, knn_clasificacion

def test_distancia_euclidiana():
    punto1 = (0, 0)
    punto2 = (3, 4)
    assert distancia_euclidiana(punto1, punto2) == 5

def test_k_vecinos_mas_cercanos():
    data = [(1, 2, 'A'), (3, 4, 'B'), (5, 6, 'A'), (7, 8, 'B')]
    punto = (1, 1)
    k = 2
    assert k_vecinos_mas_cercanos(data, punto, k) == [(1, 2, 'A'), (3, 4, 'B')]

def test_clasificar():
    vecinos = [(1, 2, 'A'), (1, 2, 'A'), (3, 4, 'B'), (3, 4, 'B'), (3, 4, 'B')]
    assert clasificar(vecinos) == 'B'

def test_knn_clasificacion():
    data = [(1, 2, 'A'), (3, 4, 'B'), (5, 6, 'A'), (7, 8, 'B')]
    punto = (1, 1)
    k = 2
    assert knn_clasificacion(data, punto, k) == 'A'
