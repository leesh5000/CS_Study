#include <iostream>

/* Implementation of Binary Max Heap using Array

 ** 구현에 앞서 **
 1. 이진힙 구현은 배열로 하고, 편의를 위해서 배열의 0번 인덱스는 비워둔다.
 2. 구현의 편의성을 위해, 노드의 데이터 값이 곧 힙 트리의 우선순위이다.
 
 - 배열의 0번 인덱스를 비워두면, 다음과 같은 이점이 생긴다.
 1. 왼쪽 자식노드의 인덱스 = 부모노드의 인덱스 * 2
 2. 오른쪽 자식노드의 인덱스 = 부모노드의 인덱스 * 2 + 1
 3. 부모노드의 인덱스 = 자식노드의 인덱스 / 2 (단, 소수점 이하는 버린다)
 4. 배열의 크기가 곧 마지막 노드의 인덱스이다.
 
-------------------------------------------------------------
 
 *********************************************
 *** Abstract Data Type in Binary Max Heap ***
 *********************************************
 
 1. Node* GetRoot() : 루트노드를 조회하는 함수, 루트노드의 주소값을 반환한다. // O(1)
 2. bool Search(int data) : 힙 트리 내에 인자로 받은 데이터 값을 가지는 노드가 존재하는지 탐색하는 함수, bool값을 반환한다. // O(n)
 3. void Insert(int data) : 인자로 받은 데이터 값을 가지는 노드를 생성한 후, 힙 트리에 추가하는 함수 // O(log(n))
 4. Node Delete() : 힙 트리의 루트노드를 삭제하는 함수, 삭제된 노드를 반환한다. // O(log(n))
 
*/

#define DEFAULT_SIZE    16

struct Node
{
    int _data;
};

struct Heap
{
    Node _arr[DEFAULT_SIZE];
    int _size = 0;
    int _cap = DEFAULT_SIZE;
    
    Node* GetRoot()
    {
        int root_idx = 1;
        return &_arr[root_idx];
    }
    
    bool Search(int data)
    {
        for (int i=1; i<=_size; i++) // 배열을 1부터 시작했으니
        {
            if (_arr[i]._data == data)
            {
                printf("Index of a node with %d : %d\n", data, i);
                return true;
            }
        }
        
        printf("Not found a node with %d\n", data);
        return false;
    }
    
    void Insert(int data)
    {
        // 사이즈가 꽉 차 있으면 리턴
        if (_size == _cap) return;
        
        // 새로 추가할 노드 생성
        Node new_Node;
        new_Node._data = data;
                
        // 새로 추가될 노드는 먼저 힙의 마지막 위치에 놓는다. 마지막 위치는 현재 힙 사이즈 + 1 이다.
        int now_idx = _size + 1; // 처음 인덱스는 마지막위치이다.

        while (now_idx != 1) // 현재 인덱스가 1이면, 루트노드이므로 더 이상 while문을 돌 필요가 없다.
        {
            int parent_idx = now_idx / 2; // 부모노드의 인덱스는 현재노드의 인덱스 / 2
            if (_arr[parent_idx]._data < new_Node._data) // 만약, 부모노드보다 새로 추가된 노드의 우선순위가 더 크다면
            {
                _arr[now_idx] = _arr[parent_idx]; // 부모노드를 한 레벨 내린다.

                now_idx /= 2; // 그 후, 현재 위치를 부모노드의 위치로 바꾼다.
            }

            else // 부모노드가 새로 추가된 노드보다 우선순위가 더 크다면,
            {
                break; // while문을 빠져나온다.
            }
        }

        // 제 위치를 찾았으면, 새로 추가된 노드를 추가해준다.
        _arr[now_idx] = new_Node;
        _size += 1;
    }
    
    Node Delete()
    {
        // 사이즈가 비어있으면 0번 인덱스 노드를 반환하고 리턴, 0번 인덱스 노드는 쓰레기값이 담긴 노드
        if (_size == 0) return _arr[0];

        // 먼저, 루트노드를 삭제한다. (실제 삭제는 하지 않고, 삭제되는 노드를 값복사 한다.)
        int root_idx = 1;
        Node remove_Node = _arr[root_idx];

        // 그 다음, 마지막 노드를 루트노드로 옮긴다. 단, 아직 노드의 위치가 확정되지 않았으므로 여기서 이동시키지는 말고,
        // 인덱스 값만 변경한 후, 위치가 확정되면 그때 옮긴다.
        Node last_node = _arr[_size];
        int now_idx = root_idx;
        
        while (true) // 현재 인덱스가 힙 트리의 크기와 같으면, 마지막 위치이므로 더 이상 진행할 필요가 없다.
        {
            int left_child_idx = now_idx * 2;
            int right_child_idx = now_idx * 2 + 1;
            int child_idx;
            
            if (left_child_idx > _size) // 자식노드가 없다면, 이제 그만 빠져나오기
            {
                break;
            }
            
            else if (left_child_idx == _size) // 자식노드가 왼쪽 하나만 존재한다면,
            {
                child_idx = left_child_idx;
            }
            
            else // 자식노드가 모두 존재한다면, 둘을 비교하고 우선순위가 더 큰 쪽을 child_idx로 하기
            {
                child_idx =
                _arr[left_child_idx]._data < _arr[right_child_idx]._data ? right_child_idx : left_child_idx;
            }
            
            // 이제, 자식노드의 우선순위와 마지막 노드의 우선순위를 비교한다.
            if (_arr[child_idx]._data >= last_node._data) // 자식노드의 우선순위가 더 크다면,
            {
                _arr[now_idx] = _arr[child_idx]; // 현재 인덱스에 자식노드를 넣는다.
                now_idx = child_idx; // 현재 인덱스의 레벨을 자식 인덱스로 올린다.
            }
            
            else // 마지막 노드의 우선순위가 자식노드의 우선순위보다 높다면,
            {
                break; // 반복문을 탈출한다.
            }
        }
        
        _arr[now_idx] = last_node; // 현재 인덱스에 저장해두었던 마지막 노드를 담는다.
        _size -= 1;
        
        return remove_Node;
    }
};

int main()
{
    /*
                90
              /    \
            80      72
           /  \    /  \
          30  24  15  42
         /
        21
    */
    
    Heap heap;
    
    // Insert
    puts("\n======Inseart======");
    heap.Insert(21);
    heap.Insert(72);
    heap.Insert(15);
    heap.Insert(24);
    heap.Insert(30);
    heap.Insert(80);
    heap.Insert(42);
    heap.Insert(90);
    
    // Access
    puts("\n======Access======");
    Node* root_Node = heap.GetRoot();
    printf("Root Node's data : %d\n", root_Node->_data);
    
    // Search
    puts("\n======Search======");
    heap.Search(15);
    heap.Search(99);
    
    // Delete
    puts("\n======Delete======");
    while (heap._size != 0)
        printf(" %d ", heap.Delete()._data);
    
    
    puts("\n");
    return 0;
}

/* All Output
 
 ======Inseart======

 ======Access======
 Root Node's data : 90

 ======Search======
 Index of a node with 15 : 6
 Not found a node with 99

 ======Delete======
  90  80  72  42  30  24  21  15
 
 */
