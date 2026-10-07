#include <stdio.h>

void foo(int *p, int x) {
    *p = x;  // Dereferences pointer p and assigns the value of x
}

int main() {
    int *z;
    int a = 20, b = 25;

    z = &a;      // z points to the memory address of a
    foo(z, b);   // Passes address of a and value of b (25)

    printf("%d", a); // Prints updated value of a
    return 0;
}

