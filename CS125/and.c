#include <stdio.h>

int main(void) {
    // 1. Binary inputs demo
    int a = 1;
    int b = 0;

    printf("=== Binary Inputs (a = %d, b = %d) ===\n", a, b);
    printf("Bitwise AND (a & b) : %d\n", a & b);
    printf("Logical AND (a && b): %d\n\n", a && b);

    // 2. User-editable inputs
    int c, d;

    printf("Enter value for c: ");
    if (scanf("%d", &c) != 1) {
        fprintf(stderr, "Invalid input for c.\n");
        return 1;
    }

    printf("Enter value for d: ");
    if (scanf("%d", &d) != 1) {
        fprintf(stderr, "Invalid input for d.\n");
        return 1;
    }

    printf("\n=== Custom Inputs (c = %d, d = %d) ===\n", c, d);
    printf("Bitwise AND (c & d) : %d\n", c & d);
    printf("Logical AND (c && d): %d\n", c && d);

    return 0;
}

