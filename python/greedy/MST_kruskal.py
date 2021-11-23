def MSTKruskal(V, adj) :
    n = len(V)
    group = [-1]*n
    g_num = 1
    E = []
    for i in range(n-1) :
        for j in range(i+1, n) :
            if adj[i][j] != None :
                E.append((i,j,adj[i][j]))
    
    E.sort(key= lambda e : e[2])

    ecount = 0

    for i in range(len(E)) :
        e = E[i]

        if group[e[0]] == -1 and group[e[1]] == -1 :
            group[e[0]] = g_num
            group[e[1]] = g_num
            g_num += 1
            print("간선 추가", V[e[0]],", ", V[e[1]], e[2])
            ecount += 1
        elif group[e[0]] != group[e[1]] :
            mi = min(group[e[0]], group[e[1]])
            mx = max(group[e[0]], group[e[1]])
            if mi == -1 : 
                if group[e[0]] == -1 : group[e[0]] = mx
                elif group[e[1]] == -1 : group[e[1]] = mx
            else : 
                for i in range(len(group)) :
                    if group[i] == mi : group[i] = mx
            print("간선 추가", V[e[0]],", ", V[e[1]], e[2])
            ecount += 1
        else :
            continue

vertex =  [ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [[ None,  29,None,None,None,  10,None ],
          [   29,None,  16,None,None,None,  15 ],
          [ None,  16,None,  12,None,None,None ],
          [ None,None,  12,None,  22,None,  18 ],
          [ None,None,None,  22,None,  27,  25 ],
          [   10,None,None,None,  27,None,None ],
          [ None,  15,None,  18,  25,None,None ]]

MSTKruskal(vertex, weight)
