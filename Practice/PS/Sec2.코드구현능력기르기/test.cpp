#include <iostream>

int main() {
    
    for (int i=0; i<10; i++) {
        int a = i;
        int b = a + 1;
    }

    printf("a: %d, b: %d", &a, &b);
    return 0;
}