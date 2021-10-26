def selection_sort(A) :
    n = len(A)

    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if A[j] < A[least] :
                least = j
        
        A[i], A[least] = A[least], A[i]

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
selection_sort(data)
print(data)
