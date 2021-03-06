#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <math.h>
#include <time.h>
#include <string.h>


// Insertionsort
void insertionsort(int arr[], int len)
{
  int i,j,key;
  for(j = 1; j < len; j++)
    {
      key = arr[j];
      for(i = j - 1; i >= 0 && arr[i] > key; i--)
        {
          arr[i + 1] = arr[i];
        }
      arr[i + 1] = key;
    }
}


////////////////////////////////////////////////////////////////////////////

// MergeSort
void merge(int arr1[], int arr2[], int arr[], double len1, double len2, double len)
{
  int i = 0;
  int j = 0;
  while(i + j < len)
    {
      if(j == len2 || ((i < len1) && (arr1[i] < arr2[j])))
        {
          arr[i + j] = arr1[i];
          i++;
        }
      else
        {
          arr[i + j] = arr2[j];
          j++;
        }
    }
}

void mergesort(int arr[], double len)
{
  if(len < 2) return;

  double mid = floor(len/2);
  int tmid = mid;
  double mid2 = ceil(len/2);
  int tmid2 = mid2;
  int arr1[tmid];
  int arr2[tmid2];
  for(int i = 0; i < mid; i++) arr1[i] = arr[i];
  for(int j = mid; j < len; j++) arr2[j-tmid] = arr[j];

  mergesort(arr1, mid);
  mergesort(arr2, mid2);
  merge(arr1, arr2, arr, mid, mid2, len);
}


////////////////////////////////////////////////////////////////////////////

// QuickSort

void quickSort( int[], int, int);               // void means the function quicksort does not return anything
int partition( int[], int, int);                // int means the function partition returns a int


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


////////////////////////////////////////////////////////////////////////////

// Number Generator
void number_generator(int size)
{
  srand(time(NULL));
  char f[] = ".txt";
  char s[sizeof(char)*(int)log10(size)];
  sprintf(s, "%d", size);
  strcat(s, f);

  int r;
  FILE *outfile;
  outfile = fopen(s, "w");
  for(int i = 0; i < size; i++)
    {
      r = rand();
      fprintf(outfile, "%d\n", r);
    }
  fclose(outfile);
}



////////////////////////////////////////////////////////////////////////////

// Driver program
void sorter(int size)
{
  char f[] = ".txt";
  char s[size+4];
  char t[size+18];
  char u[size+14];
  char v[size+14];
  char ins[] = "_insertionsort.txt";
  char mer[] = "_mergesort.txt";
  char qui[] = "_quicksort.txt";

  sprintf(s, "%d", size);
  sprintf(t, "%d", size);
  sprintf(u, "%d", size);
  sprintf(v, "%d", size);
  strcat(s, f);
  strcat(t, ins);
  strcat(u, mer);
  strcat(v, qui);
  
  FILE *infile;
  infile = fopen(s, "r");

  int insertion[size];
  int merge[size];
  int quick[size];

  FILE *insertionfile;
  insertionfile = fopen(t, "w");
  FILE *mergefile;
  mergefile = fopen(u, "w");
  FILE *quickfile;
  quickfile = fopen(v, "w");
  
  for(int i = 0; i < size; i++) {
      fscanf(infile, "%d", &insertion[i]);
      merge[i] = insertion[i];
      quick[i] = merge[i];
    }

  // Run insertion sort
  clock_t startIn = clock();
  insertionsort(insertion, size);
  clock_t finishIn = clock();

  double timeIn = (startIn-finishIn)/CLOCKS_PER_SEC;
  printf("Running time of Insertion: %f seconds\n", timeIn);
  
  // Run merge sort
  clock_t startMe = clock();
  mergesort(merge, size);
  clock_t finishMe = clock();

  double timeMe = (startMe-finishMe)/CLOCKS_PER_SEC;
  printf("Running time of MergeSort: %f seconds\n", timeMe);

  // Run quicksort
  clock_t startQu = clock();
  quickSort(quick, 0, size);
  clock_t finishQu = clock();

  double timeQu = (startQu-finishQu)/CLOCKS_PER_SEC;
  printf("Running time of Quicksort: %f seconds\n", timeQu);


  
  for(int j = 0; j < size; j++)
    {
      fprintf(insertionfile, "%d\n", insertion[j]);
      fprintf(mergefile, "%d\n", merge[j]);
      fprintf(quickfile, "%d\n", quick[j]);
    }
}


////////////////////////////////////////////////////////////////////////////

// Main function
int main() {

  number_generator(10);
  sorter(10);

  return 0;
}