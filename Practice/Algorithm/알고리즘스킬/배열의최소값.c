#include <stdio.h>

int Get_Min(int* a, int length) {
    int min = 2147000000;
    for (int i=0; i<length; i++) {
        if (a[i] < min) {
            min = a[i];
        }
    }
    return min;
}

int main() {
    int a[] = {10, 9, 1, 7, 20, -9};
    printf("%d", Get_Min(a, sizeof(a)/sizeof(int)));
}