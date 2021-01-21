#include <stdio.h>

int main() {
    // char str[] = {'r','o','t','a','t','o','r'};
    char str[] = {'h','e','l','l','o'};
    
    int len = sizeof(str)/sizeof(char);
    
    for (int i=0; i<len/2; i++) {
        if (str[i] != str[len-1-i]) {
            printf("x");
            break;
        }
    }
}