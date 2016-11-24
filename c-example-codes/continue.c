#include <stdio.h>

int main()
{
	int i;													// Declare variable i before use
	for(i=0; i<5; i++)
	{
		if(i>3)
			continue;

		printf("This is the %d th iteration.\n", i);
	}
}



// The printf() family of functions uses % character as a placeholder. When a % is encountered, printf reads the characters following the % to determine what to do:
// %s - Take the next argument and print it as a string
// %d - Take the next argument and print it as an int