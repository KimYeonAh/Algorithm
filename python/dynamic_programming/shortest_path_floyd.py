import copy
def shortest_path_floyd(vertex, W) :
    vsize = len(vertex)
    D = copy.deepcopy(W) 
    D = W
    
    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                if D[i][k] + D[k][j] < D[i][j] :
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)

def printD(D) :
    vsize = len(D)
    print("====================")

    for i in range(vsize) :
        for j in range(vsize) :
            if D[i][j] == INF : print(" INF ", end = '')
            else : print("%4d "%D[i][j], end = '')
        print("")

INF = 9999
vertex =    [ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [  [   0,   7, INF, INF,   3,  10, INF ],
            [   7,   0,   4,  10,   2,   6, INF ],
            [ INF,   4,   0,   2, INF, INF, INF ],
            [ INF,  10,   2,   0,  11,   9,   4 ],
            [   3,   2, INF,  11,   0,  13,   5 ],
            [  10,   6, INF,   9,  13,   0, INF ],
            [ INF, INF, INF,   4,   5, INF,   0 ]]

shortest_path_floyd(vertex, weight)
