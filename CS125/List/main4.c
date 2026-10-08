//Code By Jaideep
//DAte 8/10/26

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

// Search query in vector list L2
int find(double query, sadish *list) {
    while (list != NULL) {
        if (list->data == query) {
            return 1;
        }
        list = list->next;
    }
    return 0;
}

// Count remaining nodes in L1
int countNodes(sadish *head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}

int main() {
    // 1. Load both lists
    avyuh *lists = loadList("l1.dat", 1, 9);
    avyuh *L2    = loadList("l2.dat", 1, 7);

    // 2. Link L2 as the second node/row in the 'lists' avyuh
    lists->next = L2;

    // A single call to printList prints both rows
    printf("--- Combined avyuh (Row 1: L1, Row 2: L2) ---\n");
    printList(lists);

    // 3. Problem 62 logic accessed directly via the single avyuh
    // lists->vector is L1, lists->next->vector is L2
    sadish *ptr1 = lists->vector;
    sadish *ptr2 = lists->next->vector;

    while (ptr1 != NULL && ptr1->next != NULL) {
        double query = ptr1->next->data;
        if (find(query, ptr2)) {
            ptr1->next = ptr1->next->next;
        } else {
            ptr1 = ptr1->next;
        }
    }

    // 4. Print modified avyuh
    printf("\n--- After Problem 62 Logic (Modified avyuh) ---\n");
    printList(lists);

    printf("\nNodes remaining in L1: %d\n", countNodes(lists->vector));

    return 0;
}

