#include <stdio.h>

// Convert integer (0-15) into 4-bit binary representation: b3, b2, b1, b0
void int_to_binary(int num, int bits[], int size)
{
    for (int i = 0; i < size; i++)
        bits[size - 1 - i] = (num >> i) & 1;
}

// Target function F: sum-of-products minterms {0, 2, 4, 8, 10, 11, 12}
int target_F(int num)
{
    return (num == 0  || num == 2  || num == 4  || 
            num == 8  || num == 10 || num == 11 || num == 12);
}

// Option expressions
int eval_OptionA(int b3, int b2, int b1, int b0)
{
    return (!b1 && !b0) || (!b2 && !b0) || (b1 && !b2 && b3);
}

int eval_OptionB(int b3, int b2, int b1, int b0)
{
    return (!b1 && !b0) || (!b2 && !b0);
}

int eval_OptionC(int b3, int b2, int b1, int b0)
{
    return (!b2 && !b0) || (b1 && b2 && b3);
}

int eval_OptionD(int b3, int b2, int b1, int b0)
{
    return (!b1 && !b0) || (b1 && !b2 && b3);
}

int main()
{
    int bit[4]; // bit[0]=b3, bit[1]=b2, bit[2]=b1, bit[3]=b0
    int optA_match = 1, optB_match = 1, optC_match = 1, optD_match = 1;

    const char *exprA = "b1'b0' + b2'b0' + b1 b2' b3";
    const char *exprB = "b1'b0' + b2'b0'";
    const char *exprC = "b2'b0' + b1 b2 b3";
    const char *exprD = "b1'b0' + b1 b2' b3";

    printf("=========================================================================\n");
    printf("                    TRUTH TABLE FOR F(b3, b2, b1, b0)                    \n");
    printf("=========================================================================\n");
    printf("| Dec | b3 | b2 | b1 | b0 | F_target | Opt A | Opt B | Opt C | Opt D |\n");
    printf("|-----+----+----+----+----+----------+-------+-------+-------+-------|\n");

    for (int i = 0; i < 16; i++)
    {
        int_to_binary(i, bit, 4);
        int b3 = bit[0], b2 = bit[1], b1 = bit[2], b0 = bit[3];

        int f_target = target_F(i);
        int valA = eval_OptionA(b3, b2, b1, b0);
        int valB = eval_OptionB(b3, b2, b1, b0);
        int valC = eval_OptionC(b3, b2, b1, b0);
        int valD = eval_OptionD(b3, b2, b1, b0);

        if (valA != f_target) optA_match = 0;
        if (valB != f_target) optB_match = 0;
        if (valC != f_target) optC_match = 0;
        if (valD != f_target) optD_match = 0;

        printf("|  %2d |  %d |  %d |  %d |  %d |    %d     |   %d   |   %d   |   %d   |   %d   |\n",
               i, b3, b2, b1, b0, f_target, valA, valB, valC, valD);
    }
    printf("=========================================================================\n\n");

    printf("OPTION VERIFICATION:\n");
    printf("Option (A): %-30s -> %s\n", exprA, optA_match ? "CORRECT" : "INCORRECT");
    printf("Option (B): %-30s -> %s\n", exprB, optB_match ? "CORRECT" : "INCORRECT");
    printf("Option (C): %-30s -> %s\n", exprC, optC_match ? "CORRECT" : "INCORRECT");
    printf("Option (D): %-30s -> %s\n", exprD, optD_match ? "CORRECT" : "INCORRECT");

    printf("\nMINIMIZED BOOLEAN EXPRESSION:\n");
    if (optA_match) printf("F = %s\n", exprA);
    if (optB_match) printf("F = %s\n", exprB);
    if (optC_match) printf("F = %s\n", exprC);
    if (optD_match) printf("F = %s\n", exprD);

    return 0;
}

