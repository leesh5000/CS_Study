# Computer Architecture

## Contents
- Ch1 : [Introduction](#introduction)
  1. [Computer](#1-computer)
  2. [CPU의 역할](#2-cpu의-역할)
  3. [Intel i7 Processor](#3-intel-i7-processor)
  4. [Memory](#4-memory)
  5. [컴퓨터 내부](#5-컴퓨터의-내부)
  6. [x86 architecture](#6-x86-architecture)
  7. [32비트 프로세서, 64비트 프로세서](#7-32비트-프로세서-64비트-프로세서)

# Introduction

### 1. Computer
- 컴퓨터와 다른 전자장치와 구별되는 특징 : 컴퓨터는 프로그램 할 수 있다.
- 컴퓨터는 `Programmable Digital System`이다.
- 컴퓨터는 Sequential Machine이므로 State를 갖는다.
- CPU는 NAND,NOR(AND,OR,NOT) 게이트들의 집합이다.
- CMOS NAND Gate : NAND,NOR 게이트는 AND,OR,NOT게이트 대신에 4개의 트랜지스터(2 n-mos, 2 p-mos)로도 만들 수 있다.
- 따라서, 게이트들의 집합인 CPU는 다시말하면, 트랜지스터들의 집합이다. 

### 2. CPU의 역할
1. Fetch instruction from Memory, one by one
2. Decode instruction
3. Execute the operation : decode, perform operation, specify by the instruction, update machine state
4. Update machine state

### 3. Intel I7 processor
- 3GHz
  - 1초에 3*10^9번 진동하는 신호
  - 주기 한번에 F/F이 작동하여 명령어 실행 -> 1초에 3*10^9번 명령어 실행가능
- quad-core
  - 코어 4개가 각각 명령어 실행
- 4-issue superscalar processor
  - 한번에 4개 명령어 가져와서 해석 후 실행
- Hyperthreading
  - 매 cycle마다 2개 프로그램을 가져옴
- 3GHz * 4 * 4 * 2 -> 1초에 96*10^9번 명령어(instruction) 실행가능

### 4. Memory
- 여러 종류가 있음 `(caches, main memory, HDD, CD-ROM, DVD, ROM, FLASH, ...)`
- 캐쉬는 SRAM (파워가 공급되는한 계속 상태를 유지가능)
- 주메모리는 DRAM (상태유지를 위해 리프레쉬를 해줘야함)
- SRAM은 래치(2개의 nand게이트)로 구성, 6개의 트랜지스터
- DRAM은 트랜지스터 한 개로 구성
- SRAM이 DRAM보다 더 빠르고, 더 크고, 더 비쌈
- 메모리 중 일부는 I/O 장치에 맵핑되어 있음 -> `I/O port`

### 5. 컴퓨터의 내부
1. Processor(s)
   - CPU라고도 함
   - Fetches instruction from memory
   - Executes instructions
   - Transfer data from/to memory
2. Memory
   - 여러 종류가 있음 `(caches, main memory, HDD, CD-ROM, DVD, ROM, FLASH, ...)`
   - 프로그램과 데이터를 저장
   - 컴퓨터의 CPU+Memory = 인간의 뇌
3. I/O Devices
4. Interconnects
5. Motherboard

### 6. x86 architecture
- 인간이 한국어, 영어, 일본어, 등등이 있는것처럼 컴퓨터들도 모두 그들만의 언어가 있다.
- 가장 많이 쓰이는 인간 언어인 영어는 가장 많이 쓰이는 컴퓨터언어(machine language)의 x86에 비유할 수 있다.
- x86은 IA32(Intel 32bit instruction set Architecture)라고도 한다.
- x86은 machine language이지만, x86 architecture라고도 한다.
- 또 다른 컴퓨터 언어는 ARM, MIPS, SPARC, IA64, ... 등이 있다.
- x86(Intel pantium, i, AMD)은 주로 PC 프로세서가 사용하는 언어이다.
- x86(IA32)는 IA64와 완전히 다른 언어이다.
- MIPS 프로세서는 주로 임베디드(프린트)에 사용된다.
- ARM도 임베디드에서 자주 쓰이는 프로세서였지만 요즘에는 주로 스마트폰 프로세서가 사용하는 언어이다.

### 7. 32비트 프로세서, 64비트 프로세서
- 명령어의 길이로 구분하는 것 아님
- 32 vs 64 구분 : `Basic Unit of data for computation is xx bit`
- x86-64는 x86과 같은 macine language를 사용하지만 데이터 사이즈가 64비트로 증가했다.
- 32비트 프로세서는 최대 메모리 주소가 4GB이므로 최대 프로그램 사이즈가 4GB를 넘지못한다. 

### 8. ISA
- Define machine instruction(simply, machine language) 
- Define machine states such as regsiters and memory
- 컴퓨터를 설계하기 위해서는 컴퓨터가 쓰는 언어(machine language)를 먼저 개발해야한다.
- EX) `x86(IA32): 386 ~ Pentium III, Pentium IV`, `IA64: Itanium, ...`, 그 밖에 ARM, MIPS, 등등이 있다.

### 9. micro-architecture
- 같은 기계어를 사용하는 프로세서라도 그들의 내부 디자인은 다르다.
- 마이크로아키텍처는 내부디자인, 구현을 말한다. (cache, pipelining, ...)
- so, micro-architecture means processor internal design or implementation
- 인텔 x86 프로세서의 마이크로아키텍쳐는 80386(1st.Gen), 80486(2nd.Gen), Pentium(3rd.Gen), Pentium Pro(4th.Gen), Pentium 4(5th.Gen) 등이 있다.
  
### 10. CISC vs RISC
- ISA는 설계방법에 따라 CISC와 RISC로 나눌수 있다.
- CISC(complex instruction set computer)
  - 명령어 형식이 많음
  - 명령어의 크기가 각각 다름
  - complex operation
  - 따라서, 프로세서 설계가 어렵고 그로인해 컴퓨터 시스템이 느려짐
- RISC(redeuced instruction set computer)
  - CISC의 문제를 해결하기 위해 새로운 instruction set design인 RISC가 나옴
  - 명령어 형식이 적음
  - 명령어의 크기가 모두 같음
  - simple operation
  - Load-Stroe architectures
  - 따라서, 컴퓨터 설계가 쉬워지고 그로인해 속도도 빨라짐
  - RISC가 본격적으로 도입되는 1996년부터 컴퓨터의 성능이 거의 무어의 법칙을 따라감
  - -> 2002년부터 전력소모문제때문에 점차 성능향상 폭이 줄어듦(2002년 인텔 Pentium4 3.0GHz가 130W를 소비 -> 130W가 에어쿨링으로 제어할 수 있는 발열 마지노선, 많은 전력을 소비하므로 발열 발생)
  - -> CPU내부에 코어를 여러개 두면서 단일 CPU의 성능향상은 줄어들었지만 체감 성능은 훨씬 향상됨

### 11. Word
- Default data size for computation
  - cpu register size same as word size
 
### 12. Address
- point to a byte in memory

### 11. function of processor
- fetch instruction
- decode instruction
- read input
- do the computation
- store the result(update machin states)

### 12. Pipelining
- 명령어를 실행하는 하드웨어를 여러개의 독립적인 단계로 나누고, 이 하드웨어가 여러개의 서로다른 명령어들을 동시에 처리하도록 하는 기술
- 단계가 많아질수록 처리 속도가 높아질 수 있다.
- 이 프로세스를 여러 단계로 나눌 수 있다.
- 파이프라이닝이 없는 인텔 80386 프로세서는 한번에 한 가지 명령어만 처리한다. (sequentially)

### 13. Superscalar
- cpu 처리 속도를 높이기 위해 내부에 두개 혹은 그 이상의 명령어 파이프라인들을 포함시킨 구조
- 두 명령어 간에 레지스터와 기억장치에 대한 충돌이 없도록하기위해 하드웨어도 그 만큼 추가되어야하기 때문에 실제속도향상은 이론적인 속도향상 보다는 낮다.

### 13. 무어의 법칙
- the number of trasistors that can be integrated on a chip, will be double every 18 month.
- 3년마다 4배씩 증가

### Micro-processor
- 마이크로프로세서는 single chip processor를 말한다.
- 1998년 이전에는 하나의 칩에 프로세서 전체 회로를 설계하기에는 직접수준이 충분하지 않아서 프로세서를 회로가 프린트된 마더보드에 만들었다.
- 요즘에는 마이크로프로세서라고 불리는 single IC chip에 모든 프로세서 내부 회로들을 집어넣어 제조한다. -> 컴퓨터 크기 감소 및 가격하락
- 또한, 하나의 single IC에 여러개의 프로세서를 집어넣는다. (multicore)

### 14. ~nm
- the minimum featured size (length and width) of semiconductor process technolgy

### 15. Hyperthreading
- each core is two-way multi-threading, it has two PC(program counter), it can execute two programs every cycle
- 6core 12threading : 12 program can run in parelle


# Data-Structure

## Contents

- Set 1 : Introduction
    - [Data Types](#Data-Types)
    - [Data Structures](#Data-Structures)
    - [Abstract Data Type](#Abstract-Data-Type)
- Set 2 : Linear Structures
  - [Array](#Array)
  - [LinkedList](#LinkedList)
  - [Stack](#Stack)
  - [Queue](#Queue)
- Set 3 : Non-Linear Structures
    - [Tree](#Tree)
        - [Heap](#Heap)
        - [Priority Queue](#Priority-Queue)
- [Reference](#Reference)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

## Data Types

자료형(Data Types)이란 컴퓨터(엄밀하게 말하자면, 컴파일러나 인터프리터)에게 프로그래머가 데이터를 어떻게 사용하는지 미리 알려주는 일종의 데이터 속성을 말한다. 그렇다면 왜 프로그래머가 컴퓨터에게 미리 데이터를 어떻게 사용하는지 알려주어야할까? 즉, 자료형은 왜 필요할까? 
 
 사람은 10 + 20 과 12.5 + 21.7 과 같은 정수끼리의 덧셈과 실수끼리의 덧셈을 간단하게 해결할 수 있다. 하지만 컴퓨터는 모든 데이터를 0 과 1로만 표현하기
  때문에 해당 데이터가 정수인지 실수인지 구분하지 못한다. 그래서 사람이 미리 컴퓨터에게 데이터의 자료형을 정해주어 자료형에 맞는 연산을 할 수 있도록 도와주는 것이다.
  
또한, 자료형을 이용하면 메모리 효율을 높일 수 있는 이점이 있다. 우리가 가장 흔하게 쓰이는 자료형인 int를 예로 들어보자. int 자료형은 메모리에 32비트 공간을 차지하고 이 32비트를 이용하여 2<sup>32</sup> 총 42억개의 수를 표현할 수 있다. 만약, 우리가 42억개의 많은 수까지 표현할 필요가 없고 256개의 적은 수만 표현할 필요가 있다면 굳이 32비트 공간을 차지해가며 int 자료형을 써야할까? 이 경우에는 메모리의 8비트 공간만 차지하는 자료형을 사용하면 된다. 

### 자료형의 종류 ###
- Primitive data types (원시 자료형) : 프로그래밍 언어가 기본적으로 제공하는 데이터 타입들을 말한다. 원시 자료형은 프로그래밍 언어마다 다르지만, 기본적으로 정수를 나타내는 int, 실수를 나타내는 flaot, 문자를 나타내는 char 등이 있다. 
-  User define types (사용자 정의 자료형) : 원시 자료형만으로 충분하지 않을때, 사용자가 직접 정의하여 사용하는 자료형을 말한다. 대표적으로 C언어의 struct와 C++/Java의 class가 있다. 
- Composite data types (복합 자료형) : 복합 자료형은 둘 이상의 자료형을 조합한 것을 말한다. 이 조합 방법을 자료구조라고 한다. 기본 자료형을 복합 자료형으로 구성하면 새로운 유형이 된다. 예를들어, 정수형 데이터형을 여러개 조합하면 정수 배열을 만들어내며 이 둘은 다른 유형이다.

### Summary ###
- 자료형(Data Types)은 컴퓨터에게 프로그래머가 데이터를 어떻게 사용하는지 미리 알려주는 데이터 속성이다.

</br>[Contents](#Contents)</br></br>

## Data Structures 

자료구조(Data Structure)란 데이터들을 효율적으로 사용하기 위해 컴퓨터에 데이터를 저장, 관리, 조직하는 여러가지 방법을 말한다. 자료형의 관점에서 보면 자료구조란, 둘 이상의 자료형을 조합하는 방법을 말한다. 자료구조는 데이터를 정리하는 방식에 따라 선형구조와 비선형구조로 나뉜다.

### Summary ###
- 자료구조(Data Structure)란 데이터들을 효율적으로 사용하기 위해 컴퓨터에 데이터를 저장, 관리, 조직하는 여러가지 방법이다.

</br>[Contents](#Contents)</br></br>

## Abstract Data Type

### Abstraction ###

먼저 컴퓨터 공학에서 추상화(Abstraction)란, 주어진 문제나 대상을 특정 관점에서 중요한 부분만 추출해내는 것을 말한다. 예를들어, 수강신청시스템을 구현할 때 학생을 추상화해보자. 수강신청시스템 관점에서 볼 때, 학생의 중요한 데이터는 키나 몸무게가 아니라 학번과 이름이기 때문에 중요한 정보인 학번과 이름을 추출한다. 이러한 추상화 과정은 복잡한 문제에 대해 핵심에만 집중할 수 있게 해준다.

### Abstract Data Types ###

추상 자료형(ADT)은 어떤 대상이 가지는 값과 연산을 `사용자 입장`에서 나타낸 것을 말한다. 이 대상의 데이터가 어떻게 저장되었으며 기능이 어떤 알고리즘으로 동작하는지는 구체화하지 않는다. 추상자료형은 구현자 입장에서 데이터들의 구체적인 저장/조직 방법을 명시하는 자료구조와 반대되는 개념이다. 

예를들어, 스택의 ADT를 한번 정의해보자. 우리는 스택의 핵심이 나중에 들어간 데이터가 먼저 나오는 LIFO 순서라는 것을 알고있다고 가정하자. 그렇다면 이제 어떻게 구현할지 방법은 생각하지말고 LIFO 순서를 따르는 스택이 어떤 데이터를 가져야하며, 어떤 행위들을 해야하는지만 생각해보자. 먼저, 스택이 LIFO 순서가 되려면 스택의 맨 위에서 데이터의 삽입/삭제가 발생해야한다. 따라서, 스택의 맨 위에서 데이터를 삽입/삭제하는 ADT를 Push/Pop이라고 정의한다. 또 Push와 Pop을 실행하려면 스택의 맨 위를 가리키는 ADT도 있어야하므로 이것은 Top이라고 정의한다.

스택의 ADT
- Top : 스택의 맨 위를 가리키는 자료형
- Push( ) : Top에 데이터를 추가하는 연산
- Pop( ) : Top에 데이터를 삭제하는 연산
- Peek( ) : Top을 삭제하지 않고 조회만 하는 연산

### Summary ###
- 추상 자료형(ADT)은 어떤 대상이 가지는 값과 연산을 구체적인 구현 과정에 대한 언급은 하지않고 기능에만 집중해서 사용자 입장에서 나열한 것을 말한다.   

</br>[Contents](#Contents)</br></br>

## Array
배열은 같은 자료형들을 연속적인 위치에 나란히 저장하는 자료구조이다. 같은 자료형을 연속적으로 저장했기 때문에 배열의 첫 번째 원소의 위치만 알면 몇 번째 데이터든지 `첫번째 데이터의 위치 + 데이터의 크기 * i번째`으로 간단히 접근할 수 있다. 즉, 배열은 `Random Access(임의접근)` 가능하다.

배열의 크기는 고정되어있다. 배열이 확장을 위해 크기를 변경해야할때, 다음 메모리의 위치가 사용중인지 아닌지를 확신할 수 없기 때문에 마음대로 확장할 수 없다. 또한 배열이 고정된 크기를 받아 처음 선언될 때, 컴파일러는 이 크기를 가져와 배열의 파괴에 사용하기 때문에 마음대로 배열을 축소할 수 없다. 따라서, 배열이 확장/축소될때에는 더 큰/작은 사이즈를 갖는 다른 배열을 새로 생성한 후 배열 내의 모든 데이터들을 이동해야하는데 이때, 이사비용이 발생한다.

배열의 시간복잡도를 분석해보면 다음과 같다.
```
Access : O(1) [데이터들이 모두 인접한 위치에 저장되있기 떄문에]
Search : O(n) [배열이 모두 정렬되어있는 경우, 이진탐색을 이용하면 O(log(n))]
Insertion : O(n) [배열의 첫 번째 공간에 데이터를 삽입하여 이사비용이 발생할 때]
Deletion : O(n) [배열의 첫 번째 요소를 삭제하고 빈 공간을 없애기 위해 이사비용이 발생할 때]
```

### Implementation ###
- 배열 구현 [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/ArrayList/ArrayList.c)

### Applications of Array ###
배열의 단점은 사이즈가 고정되어있다는 점이다. 하지만, 배열을 응용하여 동적배열을 만들면 이를 해결할 수 있다. 동적배열은 배열의 사이즈가 동적으로 늘어나고 줄어들 수 있는 배열을 말하며 프로그래밍 언어마다 vector(C++), list(C#), ArrayList(java), list(python)로 제공된다.
1. 동적배열
2. 이진탐색(Binary Search) : 이진탐색이란, 정렬된 배열내에서 특정 값을 찾는 탐색 알고리즘을 말한다. [C](https://github.com/leesh5000/ComputerScience_Study/blob/master/Data%20Structure/C/ArrayList/BinarySearch.c)

### Summary ###
- 배열은 같은 종류의 데이터를 연속된 위치에 저장하는 자료구조이다.
- 배열은 임의접근(Random Access) 가능하다. 
- 배열은 고정된 크기를 갖기 때문에 삽입/삭제 시에 이사비용이 발생한다.

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

### Applications of Linked List ###
일반적으로 연결리스트라고 하면 단방향으로 연결된 연결리스트를 말한다. 연결리스트를 응용해서 양방향으로 연결하면 양방향 연결리스트라 하고, 연결리스트의 마지막 노드가 첫 노드를 가리키게 만든 것을 원형 연결리스트라고 한다.
1. 양방향 연결리스트
2. 원형 연결리스트

### Summary ###
- 연결리스트는 여러 개의 노드가 포인터에 의해 연결되어 있는 자료구조이다. 포인터에 의해 연결되어있으므로 순차접근을 하며, 데이터의 추가와 삭제가 간편하다.

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

### Applications of Stack ###
스택은 LIFO 순서 따르는 특징때문에 메모리의 스택영역, CPU 인터럽트 사이클, Redo/Undo, String Reversal, 계산기 구현 등에 응용된다.
1. 연산순서를 따르는 계산기
2. 스택을 이용한 트리 순회
3. Infix to Postfix/Prefix Conversion

### Summary ###
- 스택은 LIFO 순서를 따르는 자료구조이다.

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
1. LRU 캐시 구현
2. 데크 구현
3. Queuing Theory Simulation

### Summary ###
- 큐는 FIFO 순서를 따르는 선형 자료구조이다.
- 큐는 운영체제와 네트워크와 관련된 소프트웨어 구현에 있어서 중요한 역할을 하는 자료구조이다. 

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

### Applications of Tree ###
트리는 주로 계층적 데이터를 조작/관리하는데 많이 응용되는데 예를들면, 컴퓨터 시스템에서 파일 디렉터리 구조 등이 있다. 또한, 트리는 구현 방법에 따라 BST(Binary Search Tree), Heap, AVL/Red-Black Tree 등 여러 가지 다양한 트리로 응용될 수 있다.  
1. 수식트리의 구현
2. 이진트리의 BFS(Level Order Traversal)와 DFS(Pre/In/Postorder Traversal) 구현

### Summary ###
- 트리는 계층적 관계를 표현하는 비선형 자료구조이다.
- 이진트리는 각각의 노드가 공집합을 포함하여 최대 2개의 노드를 갖는 트리를 말한다.

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

### Applications of Heap ###
힙은 특별한 힙 속성으로 인해 최대/최소값을 구하고자 할 때 많이 사용된다. 이를 응용하면 우선순위 큐를 쉽게 구현할 수 있으며, Prim Algorithm 이나 Dijkstra's algorithm에 사용될 수 있다. 
1. 힙 정렬(Heap Sort) 구현
2. Heapify 구현

### Summary ###
- 힙은 우선순위 큐를 구현하는 가장 효율적인 방법이다.
- 이진 힙은 완전이진트리이며, 힙 속성을 만족하는 힙 데이터 구조이다.

</br>[Contents](#Contents)</br></br>

## Priority Queue
우선순위 큐는 다음 속성을 만족하는 큐의 확장판이다. 우선순위 큐는 비선형 구조가 아니지만, 앞서 배운 힙과 관련이 깊기 때문에 순서를 힙 다음으로 하였다.
1. 큐의 모든 항목들은 우선순위를 가진다.
2. 높은 우선순위를 가진 항목이 낮은 우선순위를 가진 항목보다 먼저 Dequeue 된다.
3. 만약, 두 항목이 우선순위가 같다면 먼저 들어온 항목을 Dequeue 한다.

우선순위 큐는 배열, 연결리스트, 힙으로 구현할 수 있는데 일반적으로 힙으로 구현한다. (Binomial heap, Pibonacci heap 등 여러 종류의 힙으로 우선순위 큐를 구현 가능하지만 여기서는 이진 힙이라고 가정한다.)

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

### Applications of Priority Queue ###
우선순위 큐는 운영체제, 여러 알고리즘에 많이 응용된다. 운영체제에서 ISR(인터럽트 서비스 루틴), A* 길찾기 알고리즘, 다익스트라 최단경로, Prim's algorithm 등에 많이 응용된다.
1. A* 길찾기 알고리즘
2. 다익스트라 최단 경로
3. Prim's algorithm

### Summary ###
- 우선순위 큐는 모든 항목들이 우선순위를 가지고 우선순위가 높은 항목이 먼저 나오는 큐의 확장판이다.
- 우선순위 큐는 운영체제, 여러 알고리즘에서 많이 응용된다.

</br>[Contents](#Contents)</br></br>

## Reference
- [윤성우의 열혈 자료구조](http://www.orentec.co.kr/teachlist/DA_ST_1/teach_sub1.php)
- [GeeksforGeeks](https://www.geeksforgeeks.org)
- [위키피디아 자료구조](https://en.wikipedia.org/wiki/Data_structure)



