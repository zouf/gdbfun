#include "stdio.h"
int main(int argc, char ** argv)
{
  int x = 666;
  int y= 777;
  int i = 0;
  for(i; i < 1000; i++)
  {
    x += y * i;
  }
  printf("x is %d\n", x);
}
