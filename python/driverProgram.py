import random, timeit

def number_generator(n):
	listNums = []
	for i in range(n):
		a = random.randint(0,1000)
		listNums.append(a)

	f = open('{}.txt'.format(n), 'w')
	f.write(str(listNums)[1:-1])
	f.close()

##########################################################
# Quicksort
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

##########################################################

def main():

	for i in range(1,6):
		n = 10**i
		number_generator(n)

	listLines = []
	arrayNum = []

	for i in (10, 100):							# For each file, make an array and add integers from files
		f = open('{}.txt'.format(i), 'r')
		for line in f.readlines():
			listLines = line.split(',')
			for integer in listLines:
				arrayNum.append(integer)

		# Pass the array from each file to the sorting algorithms 
		time = timeit.Timer(quicksort(arrayNum)).timeit()

		print("Input size:                        Time Cost:")
		print(i+"                                   {} ms".format(time))


if __name__ == '__main__':
	main()

