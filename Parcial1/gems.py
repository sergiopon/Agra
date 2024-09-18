"""
Nombre: Sergio Ponce Asprilla
Codigo: 895569
Curso: Árboles y Grafos
Septiembre 2024
"""
from collections import deque

def contar_gemas_seguras(mapa, inicio):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cola = deque([inicio])
    visitados = set([inicio])
    gemas_recogidas = 0
    posiciones_seguras = set()

    while cola:
        x, y = cola.popleft()
        if mapa[y][x] == 'G':
            gemas_recogidas += 1
        
        es_seguro = True
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if mapa[ny][nx] == 'T':
                es_seguro = False
        
        if es_seguro:
            posiciones_seguras.add((x, y))
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visitados and mapa[ny][nx] != '#':
                    visitados.add((nx, ny))
                    cola.append((nx, ny))

    return gemas_recogidas

def main():
    import sys
    input = sys.stdin.read
    datos = input().strip().split('\n')
    
    indice = 0
    resultados = []
    
    while indice < len(datos):
        ancho, alto = map(int, datos[indice].split())
        indice += 1
        mapa = []
        inicio = None
        
        for i in range(alto):
            linea = datos[indice + i]
            mapa.append(linea)
            if 'P' in linea:
                inicio = (linea.index('P'), i)
        
        indice += alto
        resultados.append(contar_gemas_seguras(mapa, inicio))
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()