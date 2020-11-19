# Data-Structure

## Contents

- [자료구조란?](#자료구조란?)
- Part I : 선형구조
  - [Array](#Array)
  - [LinkedList](#LinkedList)
  - [Stack](#Stack)
  - [Queue](#Queue)
- Part II : 비선형구조

[Home](https://github.com/leesh5000/ComputerScience_Study)

</br></br>

## 자료구조란?

자료구조는 컴퓨터에서 데이터들이 효율적으로 사용될 수 있도록 데이터들을 저장하는 여러가지 방법이다.</br>
자료구조는 그 구조에 따라 선형구조와 비선형구조로 나눌 수 있다.</br>

</br></br>

## Array

배열은 같은 종류의 데이터들을 연속적인 위치에 나란히 저장하는 자료구조이다. 배열 내의 모든 데이터들은 크기가 동일하기 때문에(같은 종류의 데이터이므로), 배열의 첫 번째 원소의 위치만 알면 몇 번째 데이터든지 `첫번째 데이터의 위치 + 데이터의 크기 * i번째`으로 간단히 접근할 수 있다. 즉, 배열은 `Random Access(임의접근)` 가능하다.

배열의 크기는 고정되어있다. 배열이 확장을 위해 크기를 변경해야할때, 다음 메모리의 위치가 사용중인지 아닌지를 확신할 수 없기 때문에 마음대로 확장할 수 없다. 또한 배열이 고정된 크기를 받아 처음 선언될 때, 컴파일러는 이 크기를 가져와 배열의 파괴에 사용하기 때문에 마음대로 배열을 축소할 수 없다. 따라서, 배열이 확장/축소될때에는 더 큰/작은 사이즈를 갖는 다른 배열을 새로 생성한 후 배열 내의 모든 데이터들을 이동해야하는데 이때, 이사비용이 발생한다. 

#### Time Complexity ####
```
Access : O(1) [데이터들이 모두 인접한 위치에 저장되있기 떄문에]
Search : O(n) [배열이 모두 정렬되어있는 경우, 이진탐색을 이용하면 O(log(n))]
Insertion : O(n) [배열의 첫 번째 공간에 데이터를 삽입하여 이사비용이 발생할 때]
Deletion : O(n) [배열의 첫 번째 요소를 삭제하고 빈 공간을 없애기 위해 이사비용이 발생할 때]
```

#### Summary ####
- 배열은 같은 종류의 데이터를 연속된 위치에 저장하는 자료구조이다.
- 고정된 크기를 갖는다.
- 임의접근(Random Access) 가능하다.
- 삽입/삭제 시에 이사비용이 발생한다.

#### Implementation ####
1. 배열을 이용하여 리스트 구현 [C](https://github.com/leesh5000/Data-Structure/blob/master/C/C/ArrayList/ArrayList.c)
2. 동적배열 구현

#### Applications of array ####
1. 이진탐색(Binary Search) 구현

</br>
[위로](#Contents)
</br>

## LinkedList

연결리스트는 데이터와 포인터를 갖는 노드를 포인터를 사용하여 연결한 자료구조이다. 포인터를 사용하여 연결되므로 인접한 위치에 저장되지 않는다. 이는 곧 각 데이터의 위치(주소)를 예측할 수 없음을 의미한다. 즉, 연결리스트에서 어떤 데이터에 접근하기 위해서는 무조건 첫번째 노드의 포인터를 통해서 `차례대로` 접근해야한다. 이것을 순차접근 (Sequential Access)라고 한다. 일반적으로 연결리스트의 첫 번째 노드를 `head`라고 한다. 

연결리스트는 포인터를 이용하여 연결되므로 삽입 및 삭제에 `O(1)`의 시간복잡도를 갖는다. 또한, 데이터 저장공간 이외에 포인터 저장공간도 필요하기 때문에 배열보다 저장효율이 떨어진다.

#### Time Complexity ####
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1)
Deletion : O(1)
```

#### Summary ####
- 연결리스트는 데이터와 포인터를 갖는 노드를 연결한 자료구조이다.
- 임의접근이 불가능하다.
- 삽입 및 삭제가 쉽다.

#### Implementation ####
1. 단방향 연결리스트 구현 (Singly LinkedList) [C](https://github.com/leesh5000/Data-Structure/blob/master/C/C/LinkedList/LinkedList.c)
2. 원형 연결리스트 구현 (Circular LinkedList)
3. 양방향 연결리스트 구현 (Doubly LinkedList)

#### Applications of LinkedList ####

[위로](#Contents)
</br></br>

## Stack

스택은 LIFO(Last-In First-Out) 순서를 따르는 선형 자료구조이다. 일반적으로, 스택의 맨 위를 `Top`라고 하며, `Push`, `Pop`, `Peek` 연산(Operation)을 제공한다.

#### Time Complexity ####
```
Access : O(n) [Sequential Access]
Search : O(n)
Insertion : O(1) [Top에서 삽입이 이루어지므로]
Deletion : O(1) [Top에서 삭제가 이루어지므로]
```

#### Summary ####
- 스택은 LIFO 순서를 따르는 자료구조이다.

#### Implementation  ####
1. 배열을 이용하여 스택 구현 [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/Stack/StackUsingArray.c)
2. 연결리스트를 이용하여 스택 구현

#### Applications of Stack ####
1. 계산기 구현
2. 백트래킹 문제

[위로](#Contents)
</br></br>

## Queue

큐는 FIFO(First-In First-Out) 순서를 따르는 선형 자료구조이다. 스택은 LIFO 순서를 따르는 자료구조로 데이터가 즉시 처리될 필요는 없지만, LIFO 순서로 처리되야 할 때 사용된다. 예를들어, 여러 소비자가 자원을 공유하는 경우와 두 프로세스 간에 데이터가 비동기적으로 전송되는 경우(데이터가 반드시 동시에 처리될 필요가 없을때)가 있다. 첫번째 경우는  `CPU 스케줄링` 이나 `디스크 스케줄링` 등이 있고, 두번째 경우는 `IO버퍼`, `파이프`, `서버` 등이 있다.

일반적으로 큐의 맨 앞과 맨 뒤를 `Front`, `Rear` 라고 하며, `Enqueu` 와 `Dequeue`  연산(Operation)을 제공한다.


#### Time Complexity ####
```
Access : O(n)
Search : O(n)
Insertion : O(1) [Front에서 삽입이 이루어지므로]
Deletion : O(1) [Rear에서 삭제가 이루어지므로]
```

#### Summary ####
- 큐는 FIFO 순서를 따르는 선형 자료구조이다.

#### Implementation #####
1. 배열을 이용한 큐의 구현 [Cpp](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C%2B%2B/Queue/QueueUsingArray.cpp)
2. 연결리스트를 이용한 큐의 구현
3. 원형 큐 구현

#### Applications of Queue ####
1. LRU 캐시 구현
2. 연결리스트를 이용하여 우선순위 큐 구현
3. 데크 구현

[위로](#Contents)
</br></br>
