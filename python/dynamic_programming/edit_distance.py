def edit_distance_dp(S, T, m, n) :
    E = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1) :
        E[i][0] = i
    for j in range(n+1) :
        E[0][j] = j

    for i in range(1, m+1) :
        for j in range(1, n+1) :
            if S[i-1] == T[j-1] : a = 0
            else : a = 1
            
            E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + a) # 삽입, 삭제, 대체 순서

    return E[m][n] 

S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)
print("문자열 : ", S, T )
print("편집거리 : ", edit_distance_dp(S, T, m, n))
