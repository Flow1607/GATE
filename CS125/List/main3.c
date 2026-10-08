#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

// Function 1: Load a sadish vector list directly from a filename
sadish *loadVecFile(char *filename, int n) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Could not open %s\n", filename);
        return NULL;
    }
    sadish *head = loadVec(fp, n);
    fclose(fp);
    return head;
}

// Function 2: Find function from GATE Problem 62 adapted to sadish
int find(double query, sadish *list) {
    while (list != NULL) {
        if (list->data == query) {
            return 1;
        }
        list = list->next;
    }
    return 0;
}

// Helper to count nodes
int countNodes(sadish *head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

int main() {
    // 1. Create the two vector lists
    sadish *L1 = loadVecFile("l1.dat", 9);
    sadish *L2 = loadVecFile("l2.dat", 7);

    // 2. Print initial vector lists
    printf("Vector List L1:\n");
    printVec(L1);

    printf("Vector List L2:\n");
    printVec(L2);

    // 3. Execution of Problem 62 loop
    sadish *ptr1 = L1;
    while (ptr1 != NULL && ptr1->next != NULL) {
        double query = ptr1->next->data;
        if (find(query, L2)) {
            // Remove node ptr1->next from L1
            ptr1->next = ptr1->next->next;
        } else {
            ptr1 = ptr1->next;
        }
    }

    // 4. Print modified L1 and node count
    printf("\nModified L1:\n");
    printVec(L1);

    printf("Number of nodes remaining in L1: %d\n", countNodes(L1));

    return 0;
}

