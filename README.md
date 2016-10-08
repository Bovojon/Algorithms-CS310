# Algorithms-CS310


## Overview of C

* `sizeof(type)` is used to get the actual size of a data type.

* `include<stdio.h>` - `stdio.h` is a standard input/output header file. For instance, it provides the `printf` function. 

* `int main (void)` - `int` is the type of the value the function returns. `main` indicates that the starting point of the program. Since an integer must be returned, `return 0` informs the OS that the function is error-free.  

#### Declarations
* Unlike in Python, in C variables and their types need to be declared before being used. Once set, the type cannot be changed. For example: `int count = 5`
>> All variables must be declared at the top.

#### Pointers
`int *p = &t;`

* `*` is a modifier and specifies a pointer type. `int *p` indicates that p is a pointer to an integer.

* `&` is the 'address-of' operator and is used for referencing. It produces the memory address of the data object.

#### Arrays
* To define a fixed-size array: `int A[inSizeOfArray]`. The array name is then converted to a pointer that points to the first item in the array. 

* Dynamic arrays can be produced using the `mallo` function which comes in the `stdlib.h` header. Example:

```
#include <stdlib.h> 	// declares malloc

int *a;
a = malloc(n*sizeof(int)); 		// malloc returns NULL if the allocation fails

if (a!=NULL){
	a[3] = 10;
}

free(a);
a=NULL;
```

* The memory allocated by the `malloc` function can be freed using the `free()` function. 

#### Input/Output

Inputting: `scanf();`
Outputing: `printf();`

Example:
```
#include <stdio.h>

int main() {
	int num;

	print("Enter any number: ");
	scanf("%d", &num);

	printf("Number = %d", num);

	return 0;
}

```

