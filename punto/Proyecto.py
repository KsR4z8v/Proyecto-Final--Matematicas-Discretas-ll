
import numpy as np
from Nodo import Nodo
"""
Autores
Yeferson Aguiar Dominguez -2067607
Jose Daniel Grajales Cadena-2067513
Oscar Fernando Rivera Pardo-2067730
Jose David Suarez Cardona-2067548
Fecha:24/06/22
"""

#matrices para dar los ejemplos
juego1 = np.array([
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 1, 1, 1, 1, 1, 5],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

])

juego2 = np.array([
    [1, 1, 1, 1, 5, 1],
    [1, 3, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 2, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 4]
])

juego3 = np.array([
    [1, 0, 0, 0, 0, 0, 0, 4],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 3, 1, 5],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 2, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0]
])


juego4 = np.array([
    [1 ,1 ,1 ,1 ,1 ,1, 1],
    [1 ,3 ,0, 0 ,1 ,5, 1],
    [1 ,0, 0 ,0, 1 ,0 ,1],
    [1 ,1 ,1, 0 ,0 ,0, 1],
    [1, 0 ,0 ,0 ,1, 0, 1],
    [1 ,2 ,0, 0, 1, 4, 1],
    [1 ,1 ,1, 1, 1 ,1 ,1]

])

juego5 = np.array([
[1,1,1,1,1],
[1,2,3,0,1],
[1,1,1,0,1],
[1,0,0,0,1],
[1,5,0,4,1]

])


# Busqueda por amplitud
# esta funcion hara el recorrido bfs sobre una matriz mediante la creacion de nodos y nos retornana
# una lista con las posiciones recorridas y la cantidad de nodos expandidos y creados
#//////////////////////////////////////////////////////////////////////////////////////////
# ejemplo1 bfs(juego1)->([(0, 4), (0, 5), (0, 6), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 
#4), (3, 5), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (9, 7)], 16568, 13250)
#////////////////////////////////////////////////////////////////////////////////////////
# ejemplo2 bfs(juego2)->([(5, 5), (4, 5), (4, 4), (3, 4), (2, 4), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 0)], 366, 330)
#///////////////////////////////////////////////////////////////////////////////////////
# ejemplo3 bfs(juego3)->([(7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)], 2898, 2638)
# ///////////////////////////////////////////////////////////////////////////////////////
# ejemplo4 bfs(juego4)-> ([(5, 5), (5, 4), (5, 3), (4, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1)], 32102, 23039)
# ///////////////////////////////////////////////////////////////////////////////////////
# ejemplo5 bfs(juego5)->([(3, 4), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)], 256, 209)
def bfs(matriz_juego):
    nodo_creados = 0
    nodos_expandidos = 0

    for i in range(matriz_juego.shape[0]):
        for j in range(matriz_juego.shape[1]):
            if matriz_juego[i][j] == 4:
                pos_agente = (j, i)  # x,y
                matriz_juego[i][j] = 0
                break

    raiz = Nodo(
        matriz_juego,
        pos_agente,
        [False, False, False],  # estado
        [pos_agente],  # Recorrido
        [pos_agente]  # Visitado
    )

    cola = [raiz]

    while len(cola) > 0:  # Condicion de parada
    
        nodo = cola.pop(0)
        print(nodo.posAgente())
        nodos_expandidos += 1

        if(nodo.condicionGanar()):
            return nodo.recorrido, nodo_creados, nodos_expandidos  # Retorno la solución

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # Genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            cola.append(hijo)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            cola.append(hijo)

        # Izquierda
        xI = x-1
        yI = y

        if xI >= 0 and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            cola.append(hijo)

        # Derecha
        xI = x+1
        yI = y

        if xI < matriz_juego.shape[1] and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            cola.append(hijo)
    return "no hay solución", nodo_creados, nodos_expandidos

# Busqueda por profundidad
# esta funcion hara el recorrido dfs sobre una matriz mediante la creacion de nodos y nos retornana
# una lista con las posiciones recorridas y la cantidad de nodos expandidos y creados
#//////////////////////////////////////////////////////////////////////////////////////////
# ejemplo1 dfs(juego1)->([(0, 4), (1, 4), (2, 4), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7), (9, 6), (8, 
#6), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (3, 5), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (9, 1), (9, 2), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7)], 230, 133)
#////////////////////////////////////////////////////////////////////////////////////////
# ejemplo2 dfs(juego2)->([(5, 5), (4, 5), (4, 4), (3, 4), (2, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 0)], 101, 75)
#///////////////////////////////////////////////////////////////////////////////////////
# ejemplo3 dfs(juego3)->([(7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)], 94, 54)
# ///////////////////////////////////////////////////////////////////////////////////////
# ejemplo4 dfs(juego4)-> ([(5, 5), (5, 4), (5, 3), (4, 3), (3, 3), (3, 4), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3), (3, 2), (2, 2), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1)], 115, 88)
# ///////////////////////////////////////////////////////////////////////////////////////
# ejemplo5 dfs(juego5)->([(3, 4), (2, 4), (1, 4), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1), (3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4)], 54, 31)


def dfs(matriz_juego):  # esta funcion hara el recorrido dfs sobre una matriz mediante la creacion de nodos
    nodo_creados = 0
    nodos_expandidos = 0

    for i in range(matriz_juego.shape[0]):
        for j in range(matriz_juego.shape[1]):
            if matriz_juego[i][j] == 4:
                pos_agente = (j, i)  # x,y
                matriz_juego[i][j] = 0
                break

    raiz = Nodo(
        matriz_juego,
        pos_agente,
        [False, False, False],
        [pos_agente],  # Recorrido
        [pos_agente]  # Visitado
    )

    pila = [raiz]

    while len(pila) > 0:  # Condicion de parada
        nodo = pila.pop(-1)
        nodos_expandidos += 1
        if(nodo.condicionGanar()):
            return nodo.recorrido, nodo_creados, nodos_expandidos  # Retorno la solución

        x = nodo.posAgente[0]
        y = nodo.posAgente[1]

        # Genero los hijos

        # Arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            pila.append(hijo)

        # Abajo
        xI = x
        yI = y + 1

        if yI < matriz_juego.shape[0] and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            pila.append(hijo)

        # Izquierda
        xI = x-1
        yI = y

        if xI >= 0 and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            pila.append(hijo)

        # Derecha
        xI = x+1
        yI = y

        if xI < matriz_juego.shape[1] and not((xI, yI) in nodo.nodos_visitados) and nodo.matriz[y, x] != 1:
            nodos_visitados = nodo.nodos_visitados.copy()  # Pasar por valor
            nodos_visitados.append((xI, yI))
            recorrido = nodo.recorrido.copy()  # Evitar pasa por referencia
            recorrido.append((xI, yI))
            estado = nodo.estado.copy()

            hijo = Nodo(
                nodo.matriz,  # Compartido
                (xI, yI),  # Nueva posición
                estado,
                recorrido,  # Nuevo
                nodos_visitados  # Nuevo
            )
            nodo_creados += 1
            hijo.marcar()  # Evaluar que sucede en la posición

            pila.append(hijo)
    return "no hay solución", nodo_creados, nodos_expandidos



#Descomentar para probar los ejemplos
print(bfs(juego1))
#print(bfs(juego2))
#print(bfs(juego3))
#print(bfs(juego4))
#print(bfs(juego5))

#print(dfs(juego1))
#print(dfs(juego2))
#print(dfs(juego3))
#print(dfs(juego4))
#print(dfs(juego5))
