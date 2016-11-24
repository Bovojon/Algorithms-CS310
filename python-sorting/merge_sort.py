def merge_sort (A):
    if len(A) > 1:    
        middle = len (A) // 2
        left = A[:middle]
        right = A[middle:]      # divide
        merge_sort (left)
        merge_sort (right)
        i = j = k = 0           # merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    return A
