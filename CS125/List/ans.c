#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

// Structure defined using avyuh to store degree and coefficients
typedef struct {
    int degree;     // Degree n
    avyuh *coeffs;  // avyuh matrix structure holding the coefficient list
} Polynomial;

// Function to construct powers of 'a': [1, a, a^2, ..., a^n] as an avyuh
avyuh *createPowerAvyuh(double a, int degree) {
    avyuh *mat = (avyuh *)malloc(sizeof(avyuh));
    mat->next = NULL;

    sadish *head = NULL, *tail = NULL;
    double current_power = 1.0;

    for (int i = 0; i <= degree; i++) {
        sadish *node = (sadish *)malloc(sizeof(sadish));
        node->data = current_power;
        node->next = NULL;

        if (head == NULL) {
            head = node;
            tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
        current_power *= a;
    }

    mat->vector = head;
    return mat;
}

// Function to evaluate P(a) using the inner product (Listdot)
double evaluatePolynomial(Polynomial p, double a) {
    avyuh *powers = createPowerAvyuh(a, p.degree);
    // P(a) = [a0, a1, ..., an] . [1, a, ..., a^n]
    return Listdot(p.coeffs, powers);
}

int main() {
    char buffer[1024];
    Polynomial P;
    sadish *head = NULL, *tail = NULL;
    int count = 0;
    double a;

    printf("Enter polynomial coefficients (a0 a1 a2 ... an) and press Enter:\n");
    if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Parse coefficients dynamically from the input line until '\n'
    char *ptr = buffer;
    char *endptr;
    while (*ptr != '\0' && *ptr != '\n') {
        while (*ptr == ' ' || *ptr == '\t') ptr++; // skip whitespace
        if (*ptr == '\0' || *ptr == '\n') break;

        double val = strtod(ptr, &endptr);
        if (ptr == endptr) break; // no further float found
        ptr = endptr;

        sadish *node = (sadish *)malloc(sizeof(sadish));
        node->data = val;
        node->next = NULL;

        if (head == NULL) {
            head = node;
            tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
        count++;
    }

    if (count == 0) {
        printf("No coefficients entered.\n");
        return 1;
    }

    // Wrap the vector list inside an avyuh
    avyuh *polyMat = (avyuh *)malloc(sizeof(avyuh));
    polyMat->vector = head;
    polyMat->next = NULL;

    P.degree = count - 1;
    P.coeffs = polyMat;

    printf("\nEnter floating point number a: ");
    if (scanf("%lf", &a) != 1) {
        printf("Invalid input for a.\n");
        return 1;
    }

    // Display loaded polynomial
    printf("\nPolynomial Degree n = %d\n", P.degree);
    printf("Coefficients vector (a0 to an):\n");
    printList(P.coeffs);

    // Compute P(a)
    double p_val = evaluatePolynomial(P, a);
    printf("\nValue of P(%lf) = %lf\n", a, p_val);

    return 0;
}

