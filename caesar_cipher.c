#include<string.h>
#include<stdio.h>
#include<stdlib.h>

/* Shift string by `shift` characters */
char* shift_string(char *str, int shift) {
  size_t length = strlen(str);
  for(size_t index = 0; index < length; index++) {
    str[index] += shift;
  }
  return str;
}

int main(int argc, char *argv[]) {
  int shift = strtol(argv[1], NULL, 10);
  char *str = argv[2];
  shift_string(str, shift);
  printf("%s\n", str);
	return 0;
}
