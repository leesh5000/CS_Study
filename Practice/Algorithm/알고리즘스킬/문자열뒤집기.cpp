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

/* 파이썬코드
def reverse_pythonic(s):
    s = s[::-1]
    return s

def reverse(s):
    for i in range(0, len(s)//2):
        temp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = temp
    return s

print(reverse_pythonic('hello'))
*/