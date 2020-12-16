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
- [Hash Table](#Hash-Table)
- [Reference](#Reference)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Data Types
- 자료형은 프로그래머가 컴퓨터에게 미리 데이터를 어떻게 사용하는지 알려주는 데이터 속성이다.

#### 자료형의 종류
- Primitive data types (원시 자료형) : 프로그래밍 언어가 기본적으로 제공하는 데이터 타입, `int, byte, ...`
-  User define types (사용자 정의 자료형) : 사용자가 직접 정의하여 사용하는 자료형을 말한다. `class, struct, ...`
- Composite data types (복합 자료형) : 복합 자료형은 둘 이상의 자료형을 조합한 것을 말한다. `Array, List, ...`

</br>[Contents](#Contents)</br></br>

## Data Structures 
- 데이터들을 효율적으로 사용하기 위해 컴퓨터에 데이터를 저장, 관리, 조직하는 여러가지 방법 

#### 자료구조의 종류
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

#### 배열의 시간복잡도
```
Access : O(1) [데이터들이 모두 인접한 위치에 저장되있기 떄문에]
Search : O(n) [배열이 모두 정렬되어있는 경우, 이진탐색을 이용하면 O(log(n))]
Insertion : O(n) [배열의 첫 번째 공간에 데이터를 삽입하여 이사비용이 발생할 때]
Deletion : O(n) [배열의 첫 번째 요소를 삭제하고 빈 공간을 없애기 위해 이사비용이 발생할 때]
```

</br>[Contents](#Contents)</br></br>

## LinkedList
- 데이터와 다음 노드를 가리키는 주소를 갖는 자료구조
- 데이터 조회가 어려움
- 데이터의 추가/삭제가 쉬움

#### 연결리스트의 시간복잡도
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1)
Deletion : O(1)
```

</br>[Contents](#Contents)</br></br>

## Stack
- LIFO(Last-In First-Out)
- 프로세스 스택에 응용
- Top, Push, Pop, Peek

#### 스택의 시간복잡도
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1) [Top에서 삽입이 이루어지므로]
Deletion : O(1) [Top에서 삭제가 이루어지므로]
```

</br>[Contents](#Contents)</br></br>

## Queue
- FIFO(First-In First-Out)
- Enqueue, Dequeue
- 운영체제, 네트워크에 많이 사용(cpu스케줄링, 디스크스케줄링, ...)

#### 큐의 시간복잡도
```
Access : O(n)
Search : O(n)
Insertion : O(1) [Front에서 삭제이 이루어지므로]
Deletion : O(1) [Rear에서 가 이루어지므로]
```

</br>[Contents](#Contents)</br></br>

## Tree
- `계층적 관계(Hierarchical Relationship)`를 표현하는 자료구조
- 다른 자료구조들과 달리 데이터의 `표현`에 초점
- 이진트리(BT) : 각 노드의 자식노드가 최대 2개인 트리
- 이진탐색트리(BST) : 왼쪽 자식노드는 작은값, 오른쪽 자식노드는 큰 값
- 탐색 알고리즘에 많이 사용됨

### 이진탐색트리의 시간복잡도
- 데이터의 탐색의 시간복잡도 = O(logN) (트리가 균형잡혀 있을때)
- 

</br>[Contents](#Contents)</br></br>

## Heap
- 최대/최소값을 빠르게 찾기위해 고안된 트리 기반 자료구조
- 완전이진트리이기 때문에 노드의 개수를 알면 그 형태를 예측할 수 있다.
- 완전이진트리이므로 배열로 구현하기 편리하다.

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

## Hash Table
- Key에 데이터를 저장하는 자료구조
- key를 입력하여 해쉬함수를 통해 데이터를 바로 조회할 수 있음
- `충돌(Collision)` : 한 개 이상의 데이터가 동일한 해쉬 주소에 저장되는 경우
- 파이썬의 Dictionary
- 주요용도
  - 데이터의 저장/삭제/조회가 빈번한 경우
  - 중복확인이 필요한 경우
- 장점
  - 데이터의 저장/삭제/조회가 빠르다.
  - 데이터의 중복 확인이 빠르다.
- 단점
  - 저장공간이 많이 필요하다.
  - 빈 공간이 발생한다.
  - 해쉬 주소가 동일할 경우 충돌을 해결하기 위한 별도의 처리가 필요하다.

### 해쉬충돌 해결 알고리즘
1. Open Hashing
   1. Chaining
      - 해쉬테이블 밖에 다른 저장공간을 활용
      - 충돌이 일어난 공간에 연결리스트로 추가 연결
2. Close Hashing
   1. Linear Probing
      - 충돌이 일어날 경우, 충돌이 일어난 공간의 다음 공간에 저장
      - 장점 : 저장공간의 활용도를 높일 수 있음
      - 단점 : 데이터를 찾기 위해 순회해야할 수도 있음

### 빈번한 충돌을 개선하는 방법
- 충돌이 많으면 해쉬충돌을 해결하더라도 탐색시간이 오래걸릴수가 있음
- 테이블의 저장공간 확대하여 공간을 늘리고 탐색시간을 줄임

### 키 생성 함수와 해쉬함수
- 유명한 해쉬함수 `SHA(secure hash algorithm)`
- SHA는 어떤 데이터라도 `유일하고, 고정된 길이의 값`으로 리턴해줌
- SHA-1, SHA-256이 있으며 SHA-256이 더 안전함
- SHA를 통해 나온 결과값으로 인풋값을 추론할 수 없음

### 해쉬테이블의 시간복잡도
- 일반적인 경우(충돌이 없는 경우) : O(1)
- 최악의 경우(매번 충돌이 발생하는 경우) : O(n)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Reference
- [윤성우의 열혈 자료구조](http://www.orentec.co.kr/teachlist/DA_ST_1/teach_sub1.php)
- [GeeksforGeeks](https://www.geeksforgeeks.org)
- [위키피디아 자료구조](https://en.wikipedia.org/wiki/Data_structure)



