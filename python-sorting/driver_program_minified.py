from time import time
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quicksort
from number_generator import number_generator
if __name__ == '__main__':    
    for i in range(1,6):
        n = 10**i
        number_generator(n)
    for j in range (1,6):
        infile = open ('{}.txt'.format(10**j),'r' )
        array = []
        for line in infile.readlines():
            listLines = line.split(',')
        for integer in listLines:
            array.append(int(integer))
        array2 = array
        array3 = array
        start_merge = time()
        merge_sort(array)
        end_merge = time()
        f = open('{}_merge_sort.txt'.format(10**j), 'w')
        f.write(str(array)[1:-1])
        f.close()
        start_quick = time()
        quicksort(array2)
        end_quick = time()
        f = open('{}_quicksort.txt'.format(10**j), 'w')
        f.write(str(array2)[1:-1])
        f.close()
        start_insertion = time()
        insertion_sort(array3)
        end_insertion = time()
        f = open('{}_insertion_sort.txt'.format(10**j), 'w')
        f.write(str(array3)[1:-1])
        f.close()
        print('Input size','\t','quicksort','\t','merge_sort','\t','insertion_sort')
        print(10**j,'\t',end_quick-start_quick,'\t',end_merge-start_merge,'\t',end_insertion-start_insertion)
