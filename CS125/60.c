#include <stdio.h>

// Function to simulate the circuit for a given initial state
int simulate_circuit(int q0, int q1, int q2, int q3) {
    int start_q0 = q0, start_q1 = q1, start_q2 = q2, start_q3 = q3;
    int count = 0;

    printf("Cycle trace starting at (%d, %d, %d, %d):\n", q0, q1, q2, q3);

    do {
        printf("  Step %d: Q0=%d, Q1=%d, Q2=%d, Q3=%d\n", count + 1, q0, q1, q2, q3);

        // Next state logic: D0 = !Q3, D1 = Q0, D2 = Q1, D3 = Q2
        int next_q0 = !q3;
        int next_q1 = q0;
        int next_q2 = q1;
        int next_q3 = q2;

        q0 = next_q0;
        q1 = next_q1;
        q2 = next_q2;
        q3 = next_q3;

        count++;
    } while (!(q0 == start_q0 && q1 == start_q1 && q2 == start_q2 && q3 == start_q3));

    printf("Returned to initial state after %d distinct states.\n\n", count);
    return count;
}

int main(void) {
    // Demonstration 1: Default initialization (0, 0, 0, 0)
    simulate_circuit(0, 0, 0, 0);

    // Demonstration 2: Alternative initialization (0, 1, 0, 0)
    simulate_circuit(0, 1, 0, 0);

    // Verify all 16 possible states
    printf("Verifying all 16 possible initial states:\n");
    int all_equal_to_8 = 1;
    for (int state = 0; state < 16; state++) {
        int q0 = (state >> 0) & 1;
        int q1 = (state >> 1) & 1;
        int q2 = (state >> 2) & 1;
        int q3 = (state >> 3) & 1;

        int curr_q0 = q0, curr_q1 = q1, curr_q2 = q2, curr_q3 = q3;
        int steps = 0;
        do {
            int n_q0 = !curr_q3;
            int n_q1 = curr_q0;
            int n_q2 = curr_q1;
            int n_q3 = curr_q2;

            curr_q0 = n_q0;
            curr_q1 = n_q1;
            curr_q2 = n_q2;
            curr_q3 = n_q3;
            steps++;
        } while (!(curr_q0 == q0 && curr_q1 == q1 && curr_q2 == q2 && curr_q3 == q3));

        if (steps != 8) {
            all_equal_to_8 = 0;
        }
    }

    if (all_equal_to_8) {
        printf("Result confirmed: Every initial state produces exactly 8 distinct states.\n");
    }

    return 0;
}

