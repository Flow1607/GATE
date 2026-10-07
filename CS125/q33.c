#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 5
#define COLS 6
#define N (ROWS * COLS) // 30 elements

// Writes random distinct integers to a file (adapted from uniform())
void generate_random_data(const char *filename, int count) {
    FILE *fp = fopen(filename, "w");
    if (!fp) {
        perror("Error creating file");
        exit(EXIT_FAILURE);
    }

    int used[600] = {0};
    for (int i = 0; i < count; i++) {
        int val;
        do {
            val = rand() % 500 + 1;
        } while (used[val]); // Guarantees distinct integers
        used[val] = 1;
        fprintf(fp, "%d\n", val);
    }
    fclose(fp);
}

// Pretty prints a 2D matrix
void print_matrix(int matrix[ROWS][COLS], const char *title) {
    printf("=========================================\n");
    printf("%s\n", title);
    printf("=========================================\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%5d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Comparator for qsort to establish descending order
int cmp_descending(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);
}

// Pseudocode fun() from Q.33 returning total swap operations
int fun(int A[], int n) {
    int swap_count = 0;
    for (int i = 0; i <= n - 2; i++) {
        for (int j = 0; j <= n - i - 2; j++) {
            if (A[j] > A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                swap_count++;
            }
        }
    }
    return swap_count;
}

int main() {
    srand(time(NULL));
    const char *data_file = "matrix_data.dat";

    // 1. Generate 30 random distinct integers into the data file
    generate_random_data(data_file, N);

    // 2. Read file data into the initial matrix
    int random_matrix[ROWS][COLS];
    int A[N];

    FILE *fp = fopen(data_file, "r");
    if (!fp) {
        perror("Error reading file");
        return 1;
    }

    int idx = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            fscanf(fp, "%d", &random_matrix[i][j]);
            A[idx++] = random_matrix[i][j];
        }
    }
    fclose(fp);

    // 3. Print the randomly generated matrix
    print_matrix(random_matrix, "Randomly Generated Matrix (5x6)");

    // 4. Arrange elements in descending order as specified in Q.33
    qsort(A, N, sizeof(int), cmp_descending);

    // 5. Execute fun() and count swap operations
    int total_swaps = fun(A, N);

    // 6. Map sorted elements into the final matrix and print
    int final_matrix[ROWS][COLS];
    idx = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            final_matrix[i][j] = A[idx++];
        }
    }

    print_matrix(final_matrix, "Final Sorted Matrix (5x6, Ascending)");

    printf("Total swap operations performed by fun(): %d\n", total_swaps);

    return 0;
}

