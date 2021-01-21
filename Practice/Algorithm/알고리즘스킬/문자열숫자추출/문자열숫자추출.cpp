#include <iostream>
#include <string>
using namespace std;

int main() {
    char str[] = "g0en2Ts8e1";
    for (int i=0; i<strlen(str); i++) {
        if (str[i] >= '0' && str[i] <= '9') {
            cout<<str[i]<<' ';
        }
    }
}