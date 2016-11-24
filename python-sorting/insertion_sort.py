def insertion_sort (A):
    for i in range (1, len(A)):
        key = A[i]
        p = i
        while p > 0 and A[p - 1] > key:
            A[p] = A[p-1]
            p = p - 1
        A[p] = key
    return A
