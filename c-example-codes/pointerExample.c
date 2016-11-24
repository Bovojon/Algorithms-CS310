#include "stdio.h"

int main() {
	int n=20, *pntr;

	pntr = &n;

	printf("Address of n variable: %x\n", &n);

	printf("Address stored in pntr variable: %x\n", pntr);
	printf("Value of *pntr variable: %d\n", *pntr);

	return 0;


}