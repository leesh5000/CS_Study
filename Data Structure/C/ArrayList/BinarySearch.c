#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/*
 
 ***********************************
 *** 이진탐색(Binary Search) 알고리즘 ***
 ***********************************
 
 - 조건 : 데이터들은 정렬되어 있어야한다.

 1. BinarySearch_Recur : 재귀를 통한 이진탐색 구현
 2. BinarySearch : 반복문을 통한 이진탐색 구현
 
 - 이진탐색의 시간복잡도 : O(log(N))
(정확히 밑이 2인 log지만, 밑이 2 이던지 1000 이던지 10000..이던지 시간복잡도에서 상수값은 무시하므로 편의상 상용로그를 로그의 시간복잡도로 사용한다.)
 
 
 */


int BinarySearch_Recur(int* arr, int start, int end, int target)
{
    if (start > end)
    {
        puts("No data found");
        return INT_MIN;
    }
    
    int mid = (start + end)/2;
    
    if (arr[mid] == target)
    {
        printf("Target data index = %d\n", mid);
        return mid;
    }
    else if (arr[mid] < target) { return BinarySearch_Recur(arr, mid+1, end, target); }
    else { return BinarySearch_Recur(arr, start, mid-1, target); }
}

int BinarySearch(int* arr, int start, int end, int target)
{
    while(start <= end)
    {
        int mid = (start + end)/2;
        
        if (arr[mid] == target)
        {
            printf("Target data index = %d\n", mid);
            return mid;
        }
        else if (arr[mid]<target) { start = mid + 1; }
        else { end = mid - 1; }
    }
    
    puts("no data found");
    return INT_MIN;
}

int main()
{
    int arr[10] = {1,2,3,7,10,11,15,23,41,80}; //
    
    /* Test1 */
    {
        printf("-----Test 1-----\n");
        int target[5] = {1,8,11,20,80};
        for (int i=0; i<sizeof(target)/sizeof(int); i++) { BinarySearch_Recur(arr, 0, 9, target[i]); }
    }
    
    /* Test2 */
    {
        printf("\n-----Test 2-----\n");
        int target[5] = {1,8,11,20,80};
        for (int i=0; i<sizeof(target)/sizeof(int); i++) { BinarySearch(arr, 0, 9, target[i]); }
    }

    return 0;
}

/* Output
 
 -----Test1-----
 Target data index = 0
 No data found
 Target data index = 5
 No data found
 Target data index = 9

 -----Test2-----
 Target data index = 0
 no data found
 Target data index = 5
 no data found
 Target data index = 9
 
 */


