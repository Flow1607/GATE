#include <stdio.h>

// Function that takes a number, an array, and size, then fills the array with its bits
void int_to_binary_array(int num, int bits[], int size) {
    for (int i = 0; i < size; i++) {
        // Extracts bits from right to left and places them into the array
        bits[size - 1 - i] = (num >> i) & 1;
    }
}

int main() {
    printf("-------------------------\n");
    printf(" a   b   c   |   Output  \n");
    printf("-------------------------\n");

    // Loop through 0 to 7
    for (int i = 0; i < 8; i++) {
        int bit[3]; // Array to hold 3 bits
        
        // 1. Automatically convert the integer into a binary array
        int_to_binary_array(i, bit, 3);
        int output = (bit[0] && bit[1]) || (bit[1] && bit[2]) || (bit[2] && bit[0]);

        printf(" %d   %d   %d   |     %d     \n", bit[0], bit[1], bit[2], output);
    }

    return 0;
}

