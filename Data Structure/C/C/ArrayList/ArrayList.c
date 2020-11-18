#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

/* Implementation ArrayList using Array
 
 ** Abstract Data Type in ArrayList **
 1. ArrayList* createArrayList(unsigned capacity) : 주어진 크기로 리스트를 생성하는 함수
 2. void Add(ArrayList* arrayList, Data data) : 리스트의 맨 끝에 데이터 추가하는 함수
 3. void Insert(ArrayList* arrayList, Data data, int index) : 리스트의 중간에 데이터를 삽입하는 함수
 4. Data Remove(ArrayList* arrayList) : 리스트의 맨 마지막의 데이터를 삭제하는 함수, 삭제된 데이터를 반환한다.
 5. Data RemoveAt(ArrayList* arrayList, int index) : 리스트의 중간의 데이터를 삭제하는 함수, 삭제된 데이터를 반환한다.
 
 */

typedef enum Bool
{
    false,
    true,
} bool;

typedef int Data;

typedef struct arrayList
{
    Data* array;
    int count;
    int capacity;
} ArrayList;

bool IsFull(ArrayList* arrayList)
{
    if (arrayList->count == arrayList->capacity) return true;
    else return false;
}

bool IsEmpty(ArrayList* arrayList)
{
    if (arrayList->count == 0) return true;
    else return false;
}

ArrayList* createArrayList(unsigned capacity)
{
    ArrayList* arrayList = (ArrayList*)malloc(sizeof(ArrayList));
    
    arrayList->array = (Data*)malloc(sizeof(Data) * capacity);
    arrayList->count = 0;
    arrayList->capacity = capacity;
    
    return arrayList;
}

void Add(ArrayList* arrayList, Data data)
{
    if (IsFull(arrayList)) return;

    arrayList->array[arrayList->count++] = data;
}

void Insert(ArrayList* arrayList, Data data, int index)
{
    if (IsFull(arrayList)) return;
    
    int lastIndex = arrayList->count - 1;
    if (index > lastIndex && index < 0) return;
    
    for (int i=lastIndex; i>=index; i--) // 이사비용 발생!
    {
        arrayList->array[i+1] = arrayList->array[i];
    }
    
    arrayList->array[index] = data;
    arrayList->count++;
}

Data Remove(ArrayList* arrayList)
{
    if (IsEmpty(arrayList)) return INT_MIN;
    
    return arrayList->array[--arrayList->count];
}

Data RemoveAt(ArrayList* arrayList, int index)
{
    if (IsEmpty(arrayList)) return INT_MIN;

    int lastIndex = arrayList->count - 1;
    if (index > lastIndex && index < 0) return INT_MIN;
    
    Data removeData = arrayList->array[index];
    
    for (int i=index; i<lastIndex; i++) // 이사비용 발생!
    {
        arrayList->array[i] = arrayList->array[i+1];
    }
    
    arrayList->count--;
    
    return removeData;
}

int main()
{
    ArrayList* arrayList = createArrayList(100);
    
    Add(arrayList, 10);
    Add(arrayList, 20);
    Add(arrayList, 30);
    Add(arrayList, 40);
    Insert(arrayList, 99, 2);
    Insert(arrayList, 999, 0);
    Remove(arrayList);
    RemoveAt(arrayList, 2);
    
    printf("ArrayList Data : ");
    for (int i=0; i<arrayList->count; i++)
        printf("%d ", arrayList->array[i]);
    puts("\n");
    
    return 0;
}

/* All Output
 
 ArrayList Data : 999 10 99 30

 Program ended with exit code: 0
 
 */
