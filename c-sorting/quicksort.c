#include <stdio.h>

// Declare functions quicksort and partition
void quickSort( int[], int, int);               // void means the function quicksort does not return anything
int partition( int[], int, int);                // int means the function partition returns a int




// Main function that calls quicksort()
void main() {
	int a[] = { 6, 13, 1, 3, 0, 15, 4, 11, 9, 23, 67, 32, 100, 54};    // Build an array of integers

	int i;                                         // Declare int i before use
  // int * p = a;                                   // Access pointer to memory allocation of array a
  int end = sizeof(a)/sizeof(*a);                           // length of the array is the size of the pointer p to a. Just calling sizeof(a) will give the size of the pointer and not of the array, since the array will decay into a pointer
	int lastIteration = end+1;
  quickSort( a, 0, end);

	printf("\n\nSorted array is:  ");
	for(i = 0; i < (lastIteration); ++i)
		printf(" %d ", a[i]);
}



// Quicksort function
void quickSort( int a[], int l, int r) {
   int j;
   if( l < r ) {
      j = partition( a, l, r);              // Partition array around first element  
     quickSort( a, l, j-1);                 // Apply Quicksort on left of pivot
     quickSort( a, j+1, r);                 // Apply quicksort on right of pivot
   }
}

// Partition function
int partition( int a[], int l, int r) {
   int pivot, i, j, t;                            // Declare all variables before use
   pivot = a[l];                                  // Select first element as pivot
   i = l; j = r+1;
		
   while( 1) {
   	do ++i; while( a[i] <= pivot && i <= r );     // ++i means increment the value of i, and then return the incremented value.
   	do --j; while( a[j] > pivot );
   	if( i >= j ) break;
   	t = a[i]; a[i] = a[j]; a[j] = t;
   }
   t = a[l]; a[l] = a[j]; a[j] = t;
   return j;
}

