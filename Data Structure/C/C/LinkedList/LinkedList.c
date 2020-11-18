#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

/* Implementation of Singly LinkedList
 
 ****************************************
 *** Abstract Data Type in LinkedList ***
 ****************************************

 1. LinkedList* CreateLinkedList() : 연결리스트 생성하는 함수
 2. void AddLast(LinkedList* linkedList, Data data) : 연결리스트 맨 마지막에 해당 data를 갖는 노드를 추가하는 함수
 3. void Insert(LinkedList* linkedList, Node* node, Data data) : 해당 Node의 뒤에 data를 갖는 노드 생성하는 함수
 4. Node* Find(LinkedList* linkedList, Data data) : 해당 data를 갖는 노드를 찾아서 반환하는 함수
 5. void Remove(LinkedList* linkedList, Data data) : 해당 data를 갖는 노드를 삭제하는 함수
 6. void PrintList(LinkedList* linkedList) : 리스트 출력 함수
 
 */

typedef enum Bool
{
    false,
    true,
} bool;

typedef int Data;

typedef struct node
{
    Data data;
    struct node* next;
} Node;

typedef struct linkedList
{
    Node* head;
    int count;
} LinkedList;

LinkedList* CreateLinkedList()
{
    LinkedList* linkedList = (LinkedList*)malloc(sizeof(LinkedList));
    
    linkedList->head = NULL;
    linkedList->count = 0;
    
    return linkedList;
}

Node* CreateNode(Data data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    
    return newNode;
}

void AddLast(LinkedList* linkedList, Data data)
{
    Node* newNode = CreateNode(data);
    
    if (linkedList->head == NULL)
        linkedList->head = newNode;
    
    else
    {
        Node* tail = linkedList->head;
        
        while (tail->next != NULL)
            tail = tail->next;
        
        tail->next = newNode;
    }
    
    linkedList->count++;
}

void Insert(LinkedList* linkedList, Node* targetNode, Data data)
{
    if (targetNode==NULL)
    {
        puts("targetNode cannot be NULL");
        return;
    }
    
    Node* newNode = CreateNode(data);
    
    newNode->next = targetNode->next; // Time Complexity of Insertion is O(1)
    targetNode->next = newNode;
}

Node* Find(LinkedList* linkedList, Data data)
{
    Node* currentNode = linkedList->head;
    
    while (currentNode != NULL) // Time Complexity of Access is O(n)
    {
        if (currentNode->data == data)
            return currentNode;
        
        currentNode = currentNode->next;
    }
    
    puts("Not found");
    return NULL;
}

void Remove(LinkedList* linkedList, Node* targetNode)
{
    if (targetNode==NULL)
    {
        puts("targetNode cannot be NULL");
        return;
    }
    
    Node* currentNode = linkedList->head;
    if (targetNode == linkedList->head)
    {
        linkedList->head = linkedList->head->next;
        free(currentNode);
        return;
    }
    
    Node* prevNode = linkedList->head;
    while (currentNode != targetNode)
    {
        prevNode = currentNode;
        currentNode = currentNode->next;
    }
    
    prevNode->next = currentNode->next; // Time Complexity of Deletion is O(1)
    free(currentNode);
}

void PrintList(LinkedList* linkedList)
{
    Node* currentNode = linkedList->head;
    
    while (currentNode != NULL)
    {
        printf(" %d ", currentNode->data);
        currentNode = currentNode->next;
    }
    
    puts("\n");
}


int main()
{
    LinkedList* linkedList = CreateLinkedList();
    
    AddLast(linkedList, 10);
    AddLast(linkedList, 20);
    AddLast(linkedList, 30);
    Insert(linkedList, Find(linkedList, 20), 99);
    AddLast(linkedList, 40);
    
    puts("LinkedList Data : ");
    PrintList(linkedList);
    
    Node* removeNode = Find(linkedList, 30);
    Remove(linkedList, removeNode);
    puts("LinkedList Data after Deletion of 30 : ");
    PrintList(linkedList);
    
    return 0;
}

/* All Output
 
 LinkedList Data :
 10 20 99 30 40

 LinkedList Data after Deletion of 30 :
 10 20 99 40
 
 */
