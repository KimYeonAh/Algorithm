def knapSack_dp(W, wt, val, n) :
    A = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(1, n+1) :
        for w in range(1, W+1) :
            if wt[i-1] > w :
                A[i][w] = A[i-1][w]
            else :
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    
    return A[n][W]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print(knapSack_dp(W, wt, val, n))