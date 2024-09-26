from sys import stdin

MAX = 10000
adj = [[] for i in range(MAX)]
visitado = [0 for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC, posMayor = int(), 0, 0, 0
sccNodos, pilaS, pilaP, salidas, entradas = [], [], [], [], []


def gabow():
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

    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while len(pilaP)>=1 and visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if  len(pilaP)>=1 and v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        #print("SCC con indice %d: " % numSCC, end = '')
        while len(pilaS)>=1 and pilaS[-1] != v:
            a = pilaS.pop()
            #print("%d " % a, end = '')
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        a = pilaS.pop()
        #print("%d " % a)
        sccInd[a] = numSCC - 1
        sccNodos[numSCC - 1].append(a)
        pilaP.pop()

def sccMinConexiones():
    global salidas, entradas, posMayor
    salidas = [0 for i in range(numSCC)]
    entradas = [0 for i in range(numSCC)]
    
    for i in range(n):
        for j in range(len(adj[i])):
            if sccInd[i] != sccInd[adj[i][j]] :
                #print(f"i: {i}")
                #print(f"j: {j}")
                salidas[sccInd[i]] += 1
                entradas[sccInd[adj[i][j]]] += 1
    posMayor = entradas.index(max(entradas))

def main():
    global n
    n, m = list(map(int, stdin.readline().split()))

    for i in range(m):
        u, v = list(map(int, stdin.readline().split()))
        adj[u].append(v)

    #print("Grafo")
    #for i in range(n):
        #print("Nodo %d:" % i)
        #for j in range(len(adj[i])):
            #print("%d" % adj[i][j], end = ' ')
        #print("")

    #print("Componentes Fuertemente Conexos:")
    gabow()
    sccMinConexiones()
    """
    print (sccNodos)
    print (posMayor)
    print (salidas)
    print (entradas)
    
    print (output2)
    """
    output2 = sccNodos[posMayor]
    output22 = sorted(output2)
    output1 = len(output2)

    print (output1)
    print (" ".join(map(str,output22)))
main()