def ChangeCoin(C, w, n) :
    R = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(1, n+1) :
        for k in range(1, w+1) :
            if i == 1 : 
                R[i][k] = k 
                continue

            if C[i-1] > k :
                R[i][k] = R[i-1][k]
            else :
                pre = R[i-1][k]
                new = 1 + R[i][k-C[i-1]]
                R[i][k] = min(pre, new)
    
    return R[n][w]

C = [1, 4, 5, 10]
w = 18
n = len(C)
print(ChangeCoin(C, w, n))
