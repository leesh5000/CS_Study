// #include <stdio.h>

// void Add_value(int n)
// {
//     printf("Add_value 함수 안에서 n의 주소값 : %p\n", &n);
//     n += 1;
// }

// void Add_ref(int *n)
// {
//     printf("Add_ref 함수 안에서 n의 주소값 : %p\n", n);
//     *n += 1;
// }

// int main()
// {
//     int a = 0;
//     // int *ref_a = &a;
//     printf("a의 주소값 : %p\n", &a);
//     Add_value(a);
//     printf("Add_value 후 a의 값 : %d\n", a);
//     Add_ref(&a);
//     printf("Add_ref 후 a의 값 %d\n", a);
//     printf("%d\n", a);
//     return 0;
// }

#include <stdio.h>

void Add(int &n)
{
    n += 1;
}

int main()
{
    int a = 10;
    int &ref_a = a;

    printf("%p\n", &a);
    printf("%p\n", &ref_a);

    Add(ref_a);
    printf("%d\n", a);
    printf("%d\n", ref_a);
}