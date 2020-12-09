# Data-Structure

## Contents

- [Data Types](#Data-Types) 
- [Data Structures](#Data-Structures)
- [Abstract Data Type](#Abstract-Data-Type)
- [Array](#Array)
- [LinkedList](#LinkedList)
- [Stack](#Stack)
- [Queue](#Queue)
- [Tree](#Tree)
- [Heap](#Heap)
- [Priority Queue](#Priority-Queue)
- [Reference](#Reference)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Data Types
- 자료형은 프로그래머가 컴퓨터에게 미리 데이터를 어떻게 사용하는지 알려주는 데이터 속성이다.

### 자료형의 종류 ###
- Primitive data types (원시 자료형) : 프로그래밍 언어가 기본적으로 제공하는 데이터 타입, `int, byte, ...`
-  User define types (사용자 정의 자료형) : 사용자가 직접 정의하여 사용하는 자료형을 말한다. `class, struct, ...`
- Composite data types (복합 자료형) : 복합 자료형은 둘 이상의 자료형을 조합한 것을 말한다. `Array, List, ...`

</br>[Contents](#Contents)</br></br>

## Data Structures 
- 데이터들을 효율적으로 사용하기 위해 컴퓨터에 데이터를 저장, 관리, 조직하는 여러가지 방법 

### 자료구조의 종류
- 선형자료구조 : 배열, 연결리스트, 스택, 큐
- 비선형자료구조 : 트리, 그래프

</br>[Contents](#Contents)</br></br>

## Abstract Data Type
- 추상자료형(ADT)은 어떤 대상이 갖는 연산들을 `사용자 입장`에서 구현방법 대한 설명없이 기능만을 나열한 것
- 추상(Abstract)은 `핵심만을 추출하다`는 의미

</br>[Contents](#Contents)</br></br>

## Array
- 같은 자료형들을 연속적인 위치에 나란히 저장하는 자료구조
- 인덱스를 통해 데이터에 접근가능 `Radom Access(임의접근)`
- 배열의 크기는 변경 불가
- 데이터의 추가/삭제에 이사비용이 발생

### 배열의 시간복잡도
```
Access : O(1) [데이터들이 모두 인접한 위치에 저장되있기 떄문에]
Search : O(n) [배열이 모두 정렬되어있는 경우, 이진탐색을 이용하면 O(log(n))]
Insertion : O(n) [배열의 첫 번째 공간에 데이터를 삽입하여 이사비용이 발생할 때]
Deletion : O(n) [배열의 첫 번째 요소를 삭제하고 빈 공간을 없애기 위해 이사비용이 발생할 때]
```

### Implementation ###
- 배열 구현 [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/ArrayList/ArrayList.c)

### Applications ###
배열의 단점은 사이즈가 고정되어있다는 점이다. 하지만, 배열을 응용하여 동적배열을 만들면 이를 해결할 수 있다. 동적배열은 배열의 사이즈가 동적으로 늘어나고 줄어들 수 있는 배열을 말하며 프로그래밍 언어마다 vector(C++), list(C#), ArrayList(java), list(python)로 제공된다.
1. 동적배열
2. 이진탐색(Binary Search) : 이진탐색이란, 정렬된 배열내에서 특정 값을 찾는 탐색 알고리즘을 말한다. [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/ArrayList/BinarySearch.c)

</br>[Contents](#Contents)</br></br>

## LinkedList
연결리스트는 여러 개의 노드가 포인터에 의해 연결되어 있는 자료구조를 말한다. 이 노드는 데이터와 다음 노드를 가리키는 포인터로 구성되어있다. 포인터를 사용하여 연결되므로 인접한 위치에 저장되지 않는다. 이는 곧 각 데이터의 위치(주소)를 예측할 수 없음을 의미한다. 즉, 연결리스트에서 어떤 데이터를 찾기 위해서는 무조건 첫번째 노드의 포인터를 통해서 `차례대로` 다음 데이터에 접근해가면서 찾아야하는데 이것을 순차접근(Sequential Access)이라고 한다. 하지만, 연결리스트는 포인터를 사용함으로써 데이터의 삽입/삭제가 간단하다는 이점이 있다. 연결리스트에 데이터를 삽입하기 위해서는 단지 해당 위치에 노드를 삽입한 후 포인터로 이전, 다음 데이터와 연결만 해주기면 되기 때문이다. 이것은 데이터의 삭제에도 마찬가지이다.

연결리스트의 시간복잡도를 정리해보면 다음과 같다.
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1)
Deletion : O(1)
```

### Implementation ###
- 연결리스트 구현 [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/LinkedList/SinglyLinkedList.c)

### Applications ###
일반적으로 연결리스트라고 하면 단방향으로 연결된 연결리스트를 말한다. 연결리스트를 응용해서 양방향으로 연결하면 양방향 연결리스트라 하고, 연결리스트의 마지막 노드가 첫 노드를 가리키게 만든 것을 원형 연결리스트라고 한다.
1. 양방향 연결리스트
2. 원형 연결리스트

</br>[Contents](#Contents)</br></br>

## Stack

스택은 LIFO(Last-In First-Out) 순서를 따르는 선형 자료구조이다. 일반적인 스택의 ADT는 스택의 맨 위를 나타내는 자료형인  `Top`과 스택의 데이터 삽입/삭제를 하는 `Push`, `Pop` 연산, 그리고 스택의 Top을 조회하는 `Peek` 연산이 있다. 

스택의 시간복잡도는 다음과 같다.
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1) [Top에서 삽입이 이루어지므로]
Deletion : O(1) [Top에서 삭제가 이루어지므로]
```

### Implementation ###
스택은 배열과 연결리스트를 이용하여 구현할 수 있다.
- 배열을 이용하여 스택 구현 [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/Stack/StackUsingArray.c)
- 연결리스트를 이용하여 스택 구현

### Applications ###
스택은 LIFO 순서 따르는 특징때문에 메모리의 스택영역, CPU 인터럽트 사이클, Redo/Undo, String Reversal, 계산기 구현 등에 응용된다.
1. 연산순서를 따르는 계산기
2. 스택을 이용한 트리 순회
3. Infix to Postfix/Prefix Conversion

</br>[Contents](#Contents)</br></br>

## Queue

큐는 FIFO(First-In First-Out) 순서를 따르는 선형 자료구조이다. 일반적인 큐의 ADT는 큐의 맨 앞과 맨 뒤를 나타내는 `Front`, `Rear` 자료형과 큐의 데이터 삽입/삭제를 하는 `Enqueu` 와 `Dequeue`  연산이 있다.

큐의 시간 복잡도는 다음과 같다.
```
Access : O(n)
Search : O(n)
Insertion : O(1) [Front에서 삭제이 이루어지므로]
Deletion : O(1) [Rear에서 가 이루어지므로]
```

### Implementation ####
큐는 배열과 연결리스트로 구현할 수 있다. 배열로 큐를 구현할때는 배열이 비어있게(empty) 되는 문제 때문에 주로 원형 큐를 구현한다.
- 배열을 이용한 큐의 구현 [Cpp](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C%2B%2B/Queue/QueueUsingArray.cpp)
- 연결리스트를 이용한 큐의 구현
- 원형 큐 구현

### Applications ###
큐는 선형 자료구조로 데이터가 즉시 처리될 필요는 없지만, LIFO 순서로 처리되야 할 때 사용된다. 예를들어, 여러 소비자가 자원을 공유하는 경우와 두 프로세스 간에 데이터가 비동기적으로 전송되는 경우(데이터가 반드시 동시에 처리될 필요가 없을때)가 있다. 첫번째 경우는  `CPU 스케줄링` 이나 `디스크 스케줄링` 등이 있고, 두번째 경우는 `IO버퍼`, `파이프`, `서버` 등이 있다. 이와 같이 큐는 운영체제와 네트워크와 관련된 소프트웨어 구현에 있어서 중요한 역할을 하는 자료구조이다.
1. LRU 캐시
2. 데크
3. Queuing Theory Simulation

</br>[Contents](#Contents)</br></br>

## Tree
트리는 `계층적 관계(Hierarchical Relationship)`를 표현하는 비선형 자료구조이다. 즉, 트리는 다른 자료구조들과 달리 데이터의 저장과 삭제가 아닌 데이터의 `표현`에 초점이 맞춰져있는 자료구조이다.

#### 트리 관련 용어 #### 
```
             A           ----- Level 0 (루트노드의 레벨을 1로 하는 책들도 있다.)
          /     \  
         B       C       ----- Level 1  
      /  |  \     \
     D   E   F     G     ----- Level 2
```
- 노드 (node) : 트리를 구성하고 있는 요소 `A,B,C,D,E,F,G`
- 간선 (edge) : 노드와 노드를 연결하는 선
- 루트 노드 (root node) : 트리 구조에서 최상위에 존재하는 노드 `A`
- 단말 노드 (terminal node) : 자식 노드가 없는 노드로 잎사귀 노드(leaf node)라고도 한다. `D,E,F,G`
- 내부 노드 (Internal node) : 단말 노드를 제외한 모든 노드로 비단말 노드(nonterminal node)라고도 한다. `B,C,D,E,F,G`
- 부모 노드 : 해당 노드에 연결된 이전 노드 `D의 부모 노드는 B`
- 조상 노드 : 해당 노드에서 루트 노드까지의 경로 상에 있는 노드 `D의 조상 노드는 B,A`
- 형제 (sibling) : 같은 부모를 가지는 노드 `B,C 와 D,E,F,G`
- 노드의 차수 (degree) : 노드의 부속 트리의 수 `B의 차수는 3, A의 차수는 2`
- 트리의 차수 (degree of tree) : 트리의 최대 차수 `트리의 차수는 3`
- 노드의 깊이 : 루트노드로부터 어떤노드 까지 거쳐야하는 간선의 수 `D의 깊이는 2`
- 레벨 (level) : 같은 깊이를 가지는 노드들의 집합 `B,C의 레벨은 1`
- 트리의 높이 : 트리의 최고 레벨 `트리의 높이는 2, 루트노드의 레벨을 1로 보면 3`

### 이진 트리 (binary tree) ###
이진트리는 각각의 노드가 공집합을 포함하여 최대 2개의 노드를 갖는 트리를 말한다. 모든 노드를 방문하는 것을 `순회(Traversal)`라고 하며, 이진트리의 순회는 DFS(Depth First Search)와 BFS(Breadth First Search) 두 가지로 구현할 수 있다. 이진트리의 DFS는 트리의 레벨 순서로 노드를 방문(Level order traversal)하는 것이고, BFS는 Preorder/Inorder/Postorder의 순서로 노드를 방문하는 것이다. 

이진트리에는 구조적 형태에 따라 포화이진트리와 완전이진트리로 나눌 수 있으며, 각각은 다음과 같다. 
- 포화이진트리 (Full Binary Tree) : 모든 레벨이 꽉 찬 이진트리
```
              A
           /     \  
          B       C  
        /  \     /  \
       D    E   F    G
```
- 완전이진트리 (Complete Binary Tree) : 모든 레벨이 꽉 찬 상태는 아니지만, 마지막 레벨을 제외한 모든 레벨의 노드는 꽉 차 있으며, 마지막 레벨은 왼쪽에서 오른쪽의 순서대로 채워진 노드를 말한다. 이와같은 특성 때문에 완전이진트리에서는 노드의 개수를 알면 트리의 구조를 확정할 수 있다.
```          
              A
           /     \   
          B       C    
        /  \     /  \   
       D    E   F    G   
     /  \
    H    I
```
- 다음과 같은 노드는 이진트리는 맞지만, 완전이진트리는 아니다.
```          
             A                    A
           /   \                /   \   
          B     C              B     C
        /  \                 /   \
       D    E               D     E
        \                 /  \
         I               H    I
```

### 이진트리의 특징 ###
- 이진트리의 레벨 n에서 최대 노드의 수는 2<sup>n</sup> 이다.
- 높이 h를 가지는 이진트리의 최대 노드의 수는 2<sup>h+1</sup>-1 이다. (일부 책에선 루트노드의 레벨을 1로 보는데, 이 경우에는 2<sup>h</sup>-1 이다.)

이진트리의 시간복잡도는 다음과 같다. 여기서 트리의 순회 방법은 BFS(level order traversal)이라고 가정한다.
```
             A           
           /   \  
          B     C         
        / | \    \
       D  E  F    G     

Access : O(n) [배열과 같이 인덱스를 갖고 있지 않는 트리는 모든 노드를 방문해서 조회하려는 데이터를 찾은 후, Access 해야하기떄문에 Search의 복잡도와 같다.]
Search : O(n) [어떤 노드를 찾기 위해서는 모든 노드를 방문해서 찾아야한다.]
Insertion : O(n) [특정 노드에 자식노드를 삽입하려한다면, 먼저 탐색을 해야하기 때문에]
Deletion : O(n) [특정 노드에 자식노드를 삭제하려한다면, 먼저 탐색을 해야하기 때문에]
```

### Implementation ####
트리는 배열과 연결리스트로 구현할 수 있다. 연결리스트가 유연하기 때문에 연결리스트로 트리를 구현하는 것이 일반적이다. 하지만, 완성된 트리가 빈번한 탐색이 이루어지는 트리라면 배열로 구현하는 것도 좋은 선택이다.
- 트리 구현 (재귀적으로 순회, 루트노드가 주어졌을 때 해당 트리의 높이를 반환하는 함수 구현)
- 배열을 이용한 이진트리 구현 (연결리스트를 이용한 이진트리와 시간복잡도 비교해보기) [Java](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/Java/src/Tree/TreeUsingArray.java)
- 연결리스트를 이용하여 이진트리 구현

### Applications ###
트리는 주로 계층적 데이터를 조작/관리하는데 많이 응용되는데 예를들면, 컴퓨터 시스템에서 파일 디렉터리 구조 등이 있다. 또한, 트리는 구현 방법에 따라 BST(Binary Search Tree), Heap, AVL/Red-Black Tree 등 여러 가지 다양한 트리로 응용될 수 있다.  
1. 수식트리
2. 이진트리의 BFS(Level Order Traversal)와 DFS(Pre/In/Postorder Traversal)

</br>[Contents](#Contents)</br></br>

## Heap
힙은 다음과 같은 힙 속성(heap property)을 만족하는 트리 기반(tree-based) 자료구조이다.
- 힙 속성 : 부모 노드의 키값은 자식 노드의 키값보다 항상 크거나 같거나`(≥)` 작거나 같다`(≤)`. 부모노드의 키값이 자식노드의 키값보다 크거나 같으면 최대힙(Max Heap), 작거나 같으면 최소힙(Min Heap)이라고 한다. 이 대소관계는 오직 부모-자식 관계에서만 적용되며, 형제 관계에서는 적용되지 않는다. (조상노드가 아니라 부모노드 임에 주의!)
힙은 우선순위 큐를 구현하는 가장 효율적인 방법이다. 힙은 구현 방법에 따라 Binary Heap, Pibonacci Heap, Binomial Heap, Leftist Heap... 등 여러가지가 있으며 가장 일반적인 구현 방법은 Binary Heap이다. 일반적으로 Binary Heap과 Heap을 혼용하며 크게 구분을 두지 않는 것 같다.
 
### 이진 힙 (Binary Heap)
이진 힙(binary heap)는 이진 트리 형태를 취하는 힙 구조를 말한다. 이때, 이진트리는 다음 두 가지 속성을 만족해야한다.
1. 구조적 속성 : 이진 힙(binary heap)은 완전이진트리(complete binary tree)이다. 즉, 마지막 레벨을 제외한 모든 레벨은 꽉 차있어야하며 마지막 레벨은 왼쪽에서 오른쪽으로 채워져야 한다. 이러한 구조적 제약은 노드의 개수를 알면 힙 트리의 구조를 확정할 수 있게 해주고 이는 곧 배열로 힙을 구현할때 큰 이점을 가져다준다.
2. 힙 속성 : 부모 노드의 키값은 자식 노드의 키값보다 항상 크거나 같거나`(≥)` 작거나 같다`(≤)`. 부모노드의 키값이 자식노드의 키값보다 크거나 같으면 최대힙(Max Heap), 작거나 같으면 최소힙(Min Heap)이라고 한다. 이 대소관계는 오직 부모-자식 관계에서만 적용되며, 형제 관계에서는 적용되지 않는다.

```          
       [Max Binary Heap]                     [Min Binary Heap]
        
             120                                    10
           /     \                               /      \   
         80       40                            27       31    
        /  \     /  \                          /  \     /  \   
       66  12   32  22                        36  30   43  57   
      /  \                                   /  \
     50  27                                 60  77                                      
```

#### 이진 힙의 데이터 추가/삭제 ####
이진 힙의 장점은 최소/최대값을 `O(1)`의 시간으로 접근할 수 있다는 것 뿐만아니라, 이진 힙의 구조적 속성 덕분에 데이터의 추가/삭제 연산에도 `O(log(n))`의 복잡도를 갖는다는 것이다.
- 데이터 추가 과정
1. 먼저, 새로운 노드를 완전이진트리가 유지될 수 있도록 마지막 레벨의 가장 오른쪽에 위치시킨다.
2. 새로 추가된 노드를 부모노드와 우선순위를 비교하고 올바른 위치를 찾을때까지 반복한다.
이진 힙은 완전이진트리이므로 높이가 하나 늘어날때마다 저장 가능한 데이터의 수는 2배씩 늘어난다. 이 말은 즉, 이진힙의 높이와 데이터의 수의 관계는 `h(n) = log<sub>2</sub>(n)`의 관계를 가진다. 이진 힙의 높이는 새로 추가된 노드가 올바른 위치를 찾기 위해 비교연산을 하는 최대 횟수와 같으므로 
이진 힙 데이터 추가 과정의 시간 복잡도는 `O(log(n))` 이다. (상수부분은 무시하므로, 로그함수의 빅오 표기법은 상용로그이다.)

- 데이터 삭제 과정
1. 먼저, 루트 노드를 삭제한다.
2. 이진 힙의 마지막 노드를 루트 위치에 옮긴 후, 자식노드와 우선순위를 비교하고 올바른 위치를 찾을때까지 반복한다.
데이터 삭제 과정도 추가 과정과 똑같은 과정이므로 같은 시간 복잡도를 갖는다.

힙 트리의 시간복잡도는 다음과 같다.
```
힙은 구현 방법에 따라, 여러가지 힙이 존재하고 각각의 시간복잡도는 다르다. 여기서는 가장 대표적인 힙인 이진힙의 시간복잡도를 말한다. 
Access : O(1), O(n) [최대/최소값을 조회하는 경우는 O(1), 특정 노드를 조회하려는 경우는 O(n)]
Search : O(n) [배열과 같이 인덱스를 갖고 있지 않는 이상은 모든 노드를 방문해서 탐색하기 때문에(Sequential Access)]
Insertion : O(log(n)) [이진힙의 데이터 추가과정]
Deletion : O(log(n)) [이진힙의 데이터 삭제과정]
```

### Implementation ####
이진 힙은 배열과 연결리스트를 기반으로 구현할 수 있다. 하지만, 이진 힙은 데이터를 추가한 이후에도 완전이진트리를 유지해야하는 특징 때문에 연결리스트 보다는 배열로 구현하는 것이 일반적이다.
- 배열을 이용하여 최대 이진힙(Max Binary Heap) 구현 [C++](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C%2B%2B/Tree/Heap/HeapUsingArr.cpp)
- Binomial Heap 구현
- Pibonacci Heap 구현

### Applications ###
힙은 특별한 힙 속성으로 인해 최대/최소값을 구하고자 할 때 많이 사용된다. 이를 응용하면 우선순위 큐를 쉽게 구현할 수 있으며, Prim Algorithm 이나 Dijkstra's algorithm에 사용될 수 있다. 
1. 힙 정렬(Heap Sort)
2. Heapify

</br>[Contents](#Contents)</br></br>

## Priority Queue
우선순위 큐는 다음 속성을 만족하는 큐의 확장판이다. 우선순위 큐는 비선형 구조가 아니지만, 앞서 배운 힙과 관련이 깊기 때문에 순서를 힙 다음으로 하였다.
1. 큐의 모든 항목들은 우선순위를 가진다.
2. 높은 우선순위를 가진 항목이 낮은 우선순위를 가진 항목보다 먼저 Dequeue 된다.
3. 만약, 두 항목이 우선순위가 같다면 먼저 들어온 항목을 Dequeue 한다.

우선순위 큐는 배열, 연결리스트, 힙으로 구현할 수 있는데 일반적으로 힙으로 구현한다. (Binomial heap, Pibonacci heap 등 여러 종류의 힙으로 우선순위 큐를 구현 가능하지만 여기서는 이진 힙으로 구현하 우선순위 큐라고 가정한다.)

우선순위 큐를 힙으로 구현하는 것이 가장 효율적인 이유는 아래 시간복잡도를 비교해보면 알 수 있다.

#### 배열 기반 우선순위 큐 (우선순위가 높을수록 배열의 앞부분에 저장한다.) ####
```
Insertion : O(n) [데이터가 추가되면 배열에 저장된 모든 데이터들과 우선순위 비교 연산을해서 자리를 찾아야한다.]
Deletion : O(1) [배열의 맨 앞에 저장된 데이터를 삭제하면 된다.]
```

#### 연결리스트 기반 우선순위 큐 ####
```
Insertion : O(n) [연결리스트도 배열처럼 데이터의 우선순위를 비교 연산을해야 하므로]
Deletion : O(1) [맨 앞에 저장된 데이터를 삭제하면 된다.]
```

#### (이진)힙 기반 우선순위 큐 ####
```
Insertion : O(log(n)) [데이터가 추가되면, 힙 트리의 높이만큼 연산을 하기 때문에 데이터 추가의 복잡도는 O(log(n))이다.]
Deletion : O(log(n) [데이터 삭제도 추가와 마찬가지이다.)
```

알고리즘의 성능에 있어서 O(log(n))과 O(n)의 차이는 어마어마하기 때문에 힙 기반 우선순위 큐가 가장 효율적인 것이다.

### Implementation ####
- 배열을 이용하여 우선순위 큐 구현
- 연결리스트를 이용하여 우선순위 큐 구현
- 힙을 이용하여 우선순위 큐 구현

### Applications ###
우선순위 큐는 운영체제, 여러 알고리즘에 많이 응용된다. 운영체제에서 ISR(인터럽트 서비스 루틴), A* 길찾기 알고리즘, 다익스트라 최단경로, Prim's algorithm 등에 많이 응용된다.
1. A* 길찾기 알고리즘
2. 다익스트라 최단 경로
3. Prim's algorithm

</br>[Contents](#Contents)</br></br>

## Reference
- [윤성우의 열혈 자료구조](http://www.orentec.co.kr/teachlist/DA_ST_1/teach_sub1.php)
- [GeeksforGeeks](https://www.geeksforgeeks.org)
- [위키피디아 자료구조](https://en.wikipedia.org/wiki/Data_structure)



