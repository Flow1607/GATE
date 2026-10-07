#include <stdio.h>

int main(void) {
    // 1. Binary inputs
    int a = 1;
    int b = 0;

    printf("=== Binary Inputs (a = %d, b = %d) ===\n", a, b);
    printf("Bitwise AND (a & b) : %d\n", a & b);
    printf("Logical AND (a && b): %d\n\n", a && b);

    // 2. Non-binary input comparison
    int c;
    int d = 1;

    printf("Enter an integer greater than 1 (e.g., 8): ");
    if (scanf("%d", &c) != 1) {
        fprintf(stderr, "Invalid input.\n");
        return 1;
    }

    printf("\n=== Non-Binary Inputs (c = %d, d = %d) ===\n", c, d);
    printf("Bitwise AND (c & d) : %d  // Compares individual bits (e.g., 1000 & 0001 = 0000)\n", c & d);
    printf("Logical AND (c && d): %d  // Compares truth values (both non-zero -> true/1)\n", c && d);

    return 0;
}

