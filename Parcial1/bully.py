"""
Nombre: Sergio Ponce Asprilla
Codigo: 895569
Curso: Árboles y Grafos
Septiembre 2024
"""

import sys
from collections import deque

def bfs(grafo, grados_entrada, N):
    cola = deque()
    rango = [0] * N
    for i in range(N):
        if grados_entrada[i] == 0:
            cola.append(i)
            rango[i] = 1

    while cola:
        nodo = cola.popleft()
        for vecino in grafo[nodo]:
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)
                rango[vecino] = rango[nodo] + 1
    
    return rango

def main():
    input = sys.stdin.read
    datos = input().split()
    
    indice = 0
    T = int(datos[indice])
    indice += 1
    resultados = []
    
    for t in range(1, T + 1):
        N = int(datos[indice])
        R = int(datos[indice + 1])
        indice += 2
        
        grafo = [[] for _ in range(N)]
        grados_entrada = [0] * N
        
        for _ in range(R):
            R1 = int(datos[indice])
            R2 = int(datos[indice + 1])
            indice += 2
            grafo[R2].append(R1)
            grados_entrada[R1] += 1
        
        rango = bfs(grafo, grados_entrada, N)
        
        empleados = [(rango[i], i) for i in range(N)]
        empleados.sort()
        
        resultados.append(f"Scenario #{t}:")
        for r, emp in empleados:
            resultados.append(f"{r} {emp}")
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()