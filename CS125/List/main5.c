#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

// Search query in vector list
int find(double query, sadish *list) {
    while (list != NULL) {
        if (list->data == query) {
            return 1;
        }
        list = list->next;
    }
    return 0;
}

// Count remaining nodes in a vector list
int countNodes(sadish *head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

int main() {
    // 1. Load both lists into a single avyuh structure
    avyuh *lists = loadList("l1.dat", 1, 9);
    lists->next  = loadList("l2.dat", 1, 7);

    printf("--- Original avyuh (L1 and L2) ---\n");
    printList(lists);

    // 2. Problem 62 logic: ptr1 traverses L1, L2 passed directly without ptr2
    sadish *ptr1 = lists->vector;

    while (ptr1 != NULL && ptr1->next != NULL) {
        double query = ptr1->next->data;
        if (find(query, lists->next->vector)) {
            ptr1->next = ptr1->next->next;
        } else {
            ptr1 = ptr1->next;
        }
    }

    // 3. Print modified avyuh and final count
    printf("\n--- Modified avyuh ---\n");
    printList(lists);

    printf("\nNodes remaining in L1: %d\n", countNodes(lists->vector));

    return 0;
}

