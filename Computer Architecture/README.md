# Computer Architecture

## Contents

- Part 1 : Computer System 
    - [컴퓨터의 기본 구조](#컴퓨터의-기본-구조)
    - [데이터]
    
- Part I : 선형구조
  - [Array](#Array)
  - [LinkedList](#LinkedList)
- Part II : 비선형구조

</br></br></br>

## Computer System

</br></br>

## 컴퓨터의 기본 구조

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

#### Example in Array ####
1. [배열을 이용하여 리스트 구현](https://github.com/leesh5000/Data-Structure/blob/master/C/C/ArrayList/ArrayList.c)
2. [이진탐색(Binary Search) 구현]

</br></br>

## LinkedList

연결리스트는 데이터와 포인터를 갖는 노드를 포인터를 사용하여 연결한 자료구조이다. 포인터를 사용하여 연결되므로 인접한 위치에 저장되지는 않는다. 일반적으로 연결리스트의 가장 첫 노드를 `head`라고 한다. 연결리스트에서 데이터들은 인접한 위치에 저장되지 않기 때문에 각 데이터의 위치(주소)를 예측할 수 없다. 즉, 연결리스트에서 어떤 데이터에 접근하기 위해서는 무조건 head의 포인터를 통해서 `차례대로` 접근해야한다. 이것은 순차접근 (Sequential Access)라고 한다. 

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

#### Example in LinkedList
1. [단방향 연결리스트 구현 (Singly LinkedList)](https://github.com/leesh5000/Data-Structure/blob/master/C/C/LinkedList/LinkedList.c)
2. [원형 연결리스트 구현 (Circular LinkedList)]
3. [양방향 연결리스트 구현 (Doubly LinkedList)]
