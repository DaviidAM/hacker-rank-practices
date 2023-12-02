// Pointers

// a' = a+b
// b' = |a-b|

//Ex:
// Sample Input
// a = 4
// b = 5
//
//Sample Output
// 9
// 1

//Solution:-------------

#include <stdio.h>

void update(int *a,int *b) {
  //Code here  ----
  int diff = *a - *b > 0 ? *a - *b : -(*a - *b);
  *a = *a + *b;
  *b = diff; 
  //-----------
}

int main() {
  int a, b;
  int *pa = &a, *pb = &b;
  
  scanf("%d %d", &a, &b);
  update(pa, pb);
  printf("%d\n%d", a, b);

  return 0;
}