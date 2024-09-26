from sys import stdin

MAX = 10000
adj = [[] for i in range(MAX)]
visitado = [-1 for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC, posMayor = 0, 0, 0, 0
sccNodos, pilaS, pilaP, salidas, entradas = [], [], [], [], []

def gabow():
    global t, numSCC
    t, numSCC = 0, 0
    for i in range(n):
        sccInd[i], visitado[i] = -1, -1

    for i in range(n):
        if visitado[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC
    t += 1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    for w in adj[v]:
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while pilaP and visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if pilaP and v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        while pilaS and pilaS[-1] != v:
            a = pilaS.pop()
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        if pilaS:
            a = pilaS.pop()
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)
            pilaP.pop()

def sccMinConexiones():
    global salidas, entradas, posMayor
    salidas = [0 for i in range(numSCC)]
    entradas = [0 for i in range(numSCC)]
    
    for i in range(n):
        for j in range(len(adj[i])):
            if sccInd[i] != sccInd[adj[i][j]]:
                salidas[sccInd[i]] += 1
                entradas[sccInd[adj[i][j]]] += 1
    posMayor = entradas.index(max(entradas))

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)

    gabow()
    sccMinConexiones()
    
    output2 = sccNodos[posMayor]
    output22 = sorted(output2)
    output1 = len(output2)

    print(output1)
    print(" ".join(map(str, output22)))

main()