#include <stdio.h> 

int main() { 
	int x; /* A normal integer*/ 
	int *p; /* A pointer to an integer ("*p" is an integer, so p must be a pointer to an integer) */ 
	p = &x; /* Read it, "assign the address of x to p" */ 
	printf("Please enter a integer:\n");
	scanf( "%d", &x ); /* Put a value in x, we could also use p here */ 
	printf( "*p=%d\n", *p ); /* Note the use of the * to get the value */
	printf("p=%p\n", p); /* content of p, which is the address of x */ 
	getchar(); 
	return 0;
}


