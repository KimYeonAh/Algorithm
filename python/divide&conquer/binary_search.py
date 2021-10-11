# list = A, 찾고싶은 숫자 = key
def binary_search(A, key, low, high) :
    while low <= high :
        mid = (low + high)//2

        if A[mid] > key :
            return binary_search(A, key, low, mid - 1)
        elif A[mid] < key :
            return binary_search(A, key, mid + 1, high)
        elif A[mid] == key :
            return mid
    
    return -1

listA = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41 ,44, 49]

print(binary_search(listA, 33, 0, len(listA)-1))
