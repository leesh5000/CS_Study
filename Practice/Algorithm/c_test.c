#include <stdio.h>
void add(int* n) {
    *n += 10;
}
int main() {
    int a = 10;
    add(&a);
    printf("%d", a);
    
    return 0;
}