"""
Nombre: Sergio Ponce Asprilla
Codigo: 895569
Curso: Árboles y Grafos
Septiembre 2024
"""


import sys

def calcular_tiempo_total(y, segmentos):
    tiempo_total = 0
    for d, s in segmentos:
        if s + y <= 0:
            tiempo_total = float('inf')
        else:
            tiempo_total += d / (s + y)
    return tiempo_total

def encontrar_y(T, segmentos):
    bajo, alto = -10000, 10000
    epsilon = 1e-7

    while alto - bajo > epsilon:
        medio = (bajo + alto) / 2
        tiempo_total = calcular_tiempo_total(medio, segmentos)
        if tiempo_total > T:
            bajo = medio
        else:
            alto = medio

    y = (bajo + alto) / 2
    return y

def main():
    input = sys.stdin.read
    datos = input().strip().split()
    
    indice = 0
    while indice < len(datos):
        n = int(datos[indice])
        T = int(datos[indice + 1])
        indice += 2
        
        segmentos = []
        for _ in range(n):
            d = int(datos[indice])
            s = int(datos[indice + 1])
            segmentos.append((d, s))
            indice += 2
        
        y = encontrar_y(n, T, segmentos)
        print(f"{y:.6f}")

if __name__ == "__main__":
    main()