#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <math.h>
#include <time.h>
#include <string.h>


void number_generator(int size) {
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

int main() {
  number_generator(10);
  return 0;
}