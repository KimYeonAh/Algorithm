def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]

    while low <= high :
        while low <= right and A[low] < pivot : low += 1
        while high >= left and A[high] > pivot : high -= 1

        if low < high :
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]
    return high

def quick_sort(A, left, right) :
    if left < right :
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
quick_sort(data, 0, len(data)-1)
print(data)
