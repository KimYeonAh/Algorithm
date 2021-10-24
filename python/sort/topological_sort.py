def topological_sort(graph) :
    inDeg = {}
    for i in graph :
        inDeg[i] = 0
    for i in graph :
        for j in graph[i] :
            inDeg[j] += 1

    vlist = []
    for i in graph :
        if inDeg[i] == 0 :
            vlist.append(i)

    while vlist :
        v = vlist.pop()
        print(v, end = ' ')

        for i in graph[v] :
            inDeg[i] -= 1
            if inDeg[i] == 0 :
                vlist.append(i)


mygraph = { "A" : {"C", "D"},
            "B" : {"D", "E"},
            "C" : {"D", "F"},
            "D" : {"F"},
            "E" : {"F"},
            "F" : {},
}

topological_sort(mygraph)
