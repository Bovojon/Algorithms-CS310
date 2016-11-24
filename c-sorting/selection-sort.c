#include <stdio.h>

int selectionSort(numlist){
	int c, d, position, swap;

	// printf("Enter the number of elements\n");
	// scanf("%d", &n);
	// printf("Enter %d integers\n", n);

	int n = sizeof(numlist);

	// for (c=0; c<n; c++){
	// 	scanf("%d", &array[c]);
	// }

	for (c=0; c<(n-1); c++) {
		position=c;
		for(d=c+1; d<n; d++){
			if (numlist[position] > numlist[d]){
				position = d;
			}
		}
		if(position != c){
			swap = numlist[c];
			numlist[c] = numlist[position];
			numlist[position] = swap;		
		}
	}
	printf("Sorted List in ascending order:\n");
	for(c=0; c<n; c++){
		printf("%d\n", numlist[c]);
	}

	return 0;
}


int main(){
	int numlist[8] = {3,7,2,5,8,1,4,6}; 
	return selectionSort(numlist);
}