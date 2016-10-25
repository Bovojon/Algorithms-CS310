def partition(array, begin, end):
    pivot = begin                                           # Choose the first element as the pivot
    for i in xrange(begin+1, end+1):                        # range returns a list while xrange returns an xrange object which is an immutable sequence and takes the same amount of memory space
        if array[i] <= array[begin]:                        # For each element after the first, if it is smaller than first, place it behind the first
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1                # Get the last element
    if begin >= end:                        # Check if there is only one element
        return
    pivot = partition(array, begin, end)    # Partition the array
    quicksort(array, begin, pivot-1)        # Apply quicksort to the left of pivot
    quicksort(array, pivot+1, end)          # Apply quicksort to the right of pivot
    return array


array = [97, 200, 100, 101, 211, 107, 5, 2, 34, 677, 105, 4, 3]
array = quicksort(array)
print(array)