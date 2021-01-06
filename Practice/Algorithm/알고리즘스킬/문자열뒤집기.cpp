#include <iostream>
#include <string>
using namespace std;

void reverse(std::string& str) {
    for (int i=0; i<str.length()/2; i++) {
        char temp = str[i];
        str[i] = str[str.length()-1-i];
        str[str.length()-1-i] = temp;
    }
}

int main() {
    std::string str = "Hello Hi";
    reverse(str);
    cout<<str;
}