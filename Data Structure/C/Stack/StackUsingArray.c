#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

/* Implementation of Stack using Array
 
 ***********************************
 *** Abstract Data Type in Stack ***
 ***********************************
 
 1. void Init(Stack* stack) : 스택 초기화 함수
 2. void Push(Stack* stack, Data data) : 스택의 top에 데이터 추가하는 함수
 3. Data Pop(Stack* stack) : 스택의 top에 데이터 삭제하는 함수, 삭제된 데이터를 반환
 4. Data Peek(Stack* stack) : 스택의 top을 반환하는 함수, 삭제는 하지 않는다.
 
 */

#define STACK_LEN  10

typedef enum Bool
{
    false,
    true,
} bool;

typedef char Data;


typedef struct stack
{
    Data arr[STACK_LEN];
    int top;
} Stack;

void Init(Stack* stack)
{
    stack->top = -1;
}

void Push(Stack* stack, Data data)
{
    if (stack->top == STACK_LEN - 1) return; // Stack is full.
    
    printf("%c pushed to stack\n", data);
    stack->arr[++stack->top] = data;
}

Data Pop(Stack* stack)
{
    if (stack->top == -1) exit(1); // Stack is empty when top is equal to -1
    
    printf("%c popped from stack\n", stack->arr[stack->top]);
    return stack->arr[stack->top--];
}

Data Peek(Stack* stack)
{
    if (stack->top == -1) exit(1); // Stack is empty when top is equal to -1
    
    return stack->arr[stack->top];
}

int main()
{
    Stack stack;
    
    Init(&stack);
    Push(&stack, 'a');
    Push(&stack, 'b');
    Push(&stack, 'c');
    Push(&stack, 'd');
    Push(&stack, 'e');
    
    puts("\n--- while() Start ---");
    
    while (stack.top != -1)
        Pop(&stack);
    
    return 0;
}

/* All Output
 
 a pushed to stack
 b pushed to stack
 c pushed to stack
 d pushed to stack
 e pushed to stack

 --- while() Start ---
 e popped from stack
 d popped from stack
 c popped from stack
 b popped from stack
 a popped from stack
 
 */
