#include <stdio.h>
#include <stdbool.h>

#define NUM_STATES 8

// Input state transitions: next_state[state][X] and output_f[state][X]
const int next_state[NUM_STATES][2] = {
    {5, 1}, // A (0) -> F, B
    {3, 2}, // B (1) -> D, C
    {5, 4}, // C (2) -> F, E
    {6, 0}, // D (3) -> G, A
    {3, 2}, // E (4) -> D, C
    {5, 1}, // F (5) -> F, B
    {6, 7}, // G (6) -> G, H
    {6, 0}  // H (7) -> G, A
};

const int out_table[NUM_STATES][2] = {
    {0, 0}, // A
    {0, 0}, // B
    {0, 0}, // C
    {1, 0}, // D
    {0, 0}, // E
    {1, 1}, // F
    {0, 1}, // G
    {1, 0}  // H
};

int main(void) {
    int partition[NUM_STATES];
    int next_partition[NUM_STATES];
    int num_groups = 0;

    // Step 1: Initial P0 partition based on outputs for X = 0 and X = 1
    // Output patterns: (0,0)->0, (1,0)->1, (1,1)->2, (0,1)->3
    for (int i = 0; i < NUM_STATES; i++) {
        int o0 = out_table[i][0];
        int o1 = out_table[i][1];

        if (o0 == 0 && o1 == 0) partition[i] = 0;
        else if (o0 == 1 && o1 == 0) partition[i] = 1;
        else if (o0 == 1 && o1 == 1) partition[i] = 2;
        else if (o0 == 0 && o1 == 1) partition[i] = 3;
    }

    // Step 2: Iterative partitioning (k-equivalence)
    bool changed = true;
    while (changed) {
        changed = false;
        int group_counter = 0;
        int assigned[NUM_STATES] = {0};

        for (int i = 0; i < NUM_STATES; i++) {
            if (assigned[i]) continue;

            next_partition[i] = group_counter;
            assigned[i] = 1;

            for (int j = i + 1; j < NUM_STATES; j++) {
                if (assigned[j]) continue;

                // Two states are k-equivalent if they belong to the same group in (k-1)
                // and transition to the same group in (k-1) under all inputs
                bool same_group = (partition[i] == partition[j]);
                bool same_next_0 = (partition[next_state[i][0]] == partition[next_state[j][0]]);
                bool same_next_1 = (partition[next_state[i][1]] == partition[next_state[j][1]]);

                if (same_group && same_next_0 && same_next_1) {
                    next_partition[j] = group_counter;
                    assigned[j] = 1;
                }
            }
            group_counter++;
        }

        // Check if partition changed
        for (int i = 0; i < NUM_STATES; i++) {
            if (partition[i] != next_partition[i]) {
                changed = true;
            }
            partition[i] = next_partition[i];
        }

        num_groups = group_counter;
    }

    printf("Minimum number of states: %d\n\n", num_groups);

    // Print resulting equivalence classes
    const char state_names[] = "ABCDEFGH";
    for (int g = 0; g < num_groups; g++) {
        printf("State S%d: { ", g);
        for (int i = 0; i < NUM_STATES; i++) {
            if (partition[i] == g) {
                printf("%c ", state_names[i]);
            }
        }
        printf("}\n");
    }

    return 0;
}

