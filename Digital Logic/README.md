# Digital Logic

## Contents

- Ch 1 : [Introduction](#introduction)
- Ch 2 : [Number System](#number-system)
- Ch 3 : [Logic Gate](#logic-gate)
- Ch 4 : [Boolean Algebra](#boolean-algebra)
- Ch 5 : [SOP and POS](#sop-and-pos)
- Ch 6 : [Karnaugh Map](#karnaugh-map)
- Ch 7 : [Logic Circuit](#logic-circuit)
- Ch 8 : [Combinational Logic Circuit](#combinational-logic-circuit)
- Ch 9 : [Sequential Logic Circuit](#sequential-logic-circuit)
- [Reference](#reference)

<br>[Home](https://github.com/leesh5000/ComputerScience_Study)</br></br>

# Introduction #

## 아날로그와 디지털 ##
- 아날로그는 연속적인 값
- 디지털은 이산적인(discrete) 값

#### 아날로그 신호를 디지털 신호로 변환
1. 표본화(Sampling) : 여러 데이터 중 대표값을 선정
2. 양자화(Quantizing) : 표본화 된 데이터를 컴퓨터가 나타낼 수 있는 정확도로 근사화
3. 부호화(Encoding) : 양자화 된 데이터를 이진수로 변환

#### 디지털 시스템의 장점
- 외부환경이나 잡음에 강함
- 데이터의 저장과 가공이 편리
- 시스템 설계가 편리

<br>

## 이진값과 전압
- 연속적인 전기신호의 전압이 기준값보다 낮을 때는 0, 높을 때는 1로 이진값으로 변환
- 0->1인 부분을 `Rising Edge`, 1->0인 부분을 `Falling Edge`

#### 주기와 주파수 ####
- 주기(Period, 단위(time)) : Edge부터 다음 Edge까지 걸리는 시간
- 주파수(Frequency, 단위(Hertz)) : 1초에 진동하는 횟수
-  T = 1 / f

<br>

### 논리회로의 종류 ###
- 조합논리회로 (combinational logic circuit)
  - 기본 게이트의 조합으로 구성되는 회로 
  - `ex) 리모컨의 숫자 버튼`
- 순차논리회로 (sequential logic circuit)
  - 현재 상태를 저장하는 `저장소자`가 포함된 논리회로 
  - `ex) 리모컨의 채널 +/- 버튼`

#### 저장소자의 종류 ####
- Latch, Flip-flop
- Register (플립플롭이 여러개 모인 것)
- 메모리 : (공통점)전원을 끄면 저장되어 있던게 사라지는 휘발성 메모리
    - DRAM (dynamic random access memory)
      - 저장된 데이터가 시간이 지나면 사라지는 메모리
      - 주기적 Refresh를 해주지 않으면 데이터가 사라짐
    - SRAM (static random access memory)
      - Refresh를 하지 않아도 데이터가 사라지지 않는 메모리, 캐시 메모리로 사용한다. 
      - 가격이 비쌈

<br>[Contents](#Contents)<br><br>

# Number System
- 컴퓨터에서 주로 사용하는 수 체계는 2진수, 16진수
  - 2진수 : 0과1 두 가지 digit으로 수를 표현
  - 16진수 : 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F 16가지 digit으로 수를 표현
- 2진수 4비트를 16진수 1비트로 변환 가능 `ex) 1111(2) = F(16)`

#### MSB and LSB
- MSB (most significant bit) : 가장 왼쪽에 있는 비트
- LSB (least significant bit) : 가장 오른쪽에 있는 비트

#### 2의보수
- 컴퓨터가 음수를 표현할 때 가장많이 쓰는 방법
- `1의보수 + 1`

<br>

## 부동소수점 수(Floating Point Number)
- 컴퓨터가 실수를 표현하는데 쓰는 방법
- 소수점의 위치를 고정하지 않음
- 부동소수점 표준은 `단정도(Single Precision)`과 `배정도(Double Precision)`이 있다.
- 단정도가 32비트를 쓰는 float, 배정도가 64비트를 쓰는 double

<br>[Contents](#Contents)<br><br>

# Logic Gate
- 논리연산에 기본이 되는 논리소자
- `Gate`는 정보흐름을 결정하는 소자를 말한다.

#### 논리소자의 특징
- 입력신호들에 취해지는 논리 조합에 따라 출력이 결정된다.
- 1 이상의 논리값으로 부터 새로운 논리값을 만든다.

#### 논리소자의 구분
- 기본게이트 : NOT, AND, OR
- 범용게이트 : NAND, NOR `모든 다른 게이트들은 이 2개의 범용게이트들을 대체하여 표현 가능`
- 기타게이트 : XOR, XNOR

<br>

## Buffer
- 입력과 출력이 같은 논리게이트

#### 진리표 (A는 입력, X는 출력)
| A | X |
|:---:|:---:|
| 0 | 0 |
| 1 | 1 |

<br>

## Inverter
- 입력을 반전하여 출력하는 논리게이트
- NOT게이트 라고도 함

#### 진리표 (A는 입력, X는 출력)
| A | X |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

<br>

## AND
- 두 수의 입력이 모두 1일 경우에만 출력이 1인 논리게이트
- `논리곱(Conjunction)`

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

<br>

## OR
- 두 수의 입력 중 하나라도 1인 경우에 출력이 1 또는 두 수의 입력이 모두 0일 경우에만 0인 논리게이트
- `논리합(Disjunction)`

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

<br>

## NAND
- 두 수의 입력이 1일 경우에만 출력이 0인 논리게이트
- AND의 출력을 NOT 시킨 것
- NAND 게이트는 negative-OR 게이트와 등가

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

<br>

## NOR
- 두 수의 입력 중 하나라도 1인 경우에 출력이 0 또는 두 수의 입력이 모두 0일 경우에만 출력이 1인 논리게이트
- OR의 출력을 NOT 시킨 것 
- NOR 게이트는 negative-AND 게이트와 등가

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 0 |

<br>

## XOR
- Exlcusive-OR
- 두 수가 다를 때 출력이 1 또는 1의 개수가 홀수일 때 출력이 1인 논리게이트
- `홀수(Odd) 함수`

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

<br>

## XNOR
- Exclusive-NOR
- 두 수가 같을 때 출력이 1 또는 1의 개수가 짝수일 때 출력이 1인 논리게이트
- `짝수(Even) 함수`

#### 진리표 (A는 입력, X는 출력)
| A | B | Q |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

<br>[Contents](#Contents)<br><br>

# Boolean Algebra
- 0, 1, 논리연산(AND,OR,NOT)들을 대수화 한 것
- 부울대수는 논리회로의 관계를 표현하기에 유용다.

<br>

## 부울대수의 법칙
- 교환법칙 (Commutative Law)
  - 부울 합 (OR) : A+B = B+A
  - 부울 곱 (AND) : A•B = B•A
- 결합법칙 (Associative Law)
  - A+(B+C) = (A+B)+C
  - A•(B•C) = (A•B)•C
- 배분법칙 (Distributive Law)
  - A•(B+C) = (A•B)+(A•C)
  - A+(B•C) = (A+B)•(A+C) [일반적인 대수관계와 다르니까 주의]
- A + 0 = A
- A + 1 = 1
- A + A = A
- A + ~A = 1
- A • 0 = 0
- A • 1 = A
- A • A = A
- A • A' = 0
- (A')' = A
- A+A•B = A•(A+B)
```
Prove that,

A+A•B 
= (A+A)•(A+B)
= A•(A+B)    
```
- A+A•B = A
```
Prove that,

A+A•B 
= A•1+A•B
= A•(1+B)
= A•1    
= A      
```

<br>

## De Morgan's Theorem
- 제 1법칙 (1's Theorem)
  - (A•B)' = A'+B'
  - 변수의 곱에 대한 보수는 각 변수들의 보수의 합과 같다.
  - NAND게이트는 negative-OR게이트와 등가이다.

- 제 2법칙 (2's Theorem)
  - (A+B)' = A'•B'
  - 변수의 합에 대한 보수는 각 변수들의 보수의 곱과 같다.
  - NOR게이트는 negative-AND게이트와 등가이다.

<br>[Contents](#Contents)<br><br>

# SOP and POS
- SOP(sum of product) : 변수곱들의 합으로 이루어진 부울수식
  - SOP는 AND, OR 게이트로 이루어짐
  - 모든 부울 수식들은 SOP로 변환 가능
  - `SOP = 1`인 경우를 찾으면 빠르게 진리표 완성
- POS(product of sum) : 변수합들의 곱으로 이루어진 부울수식
  - POS와 듀얼관계
  - `POS = 0`인 경우를 찾으면 빠르게 진리표 완성

<br>[Contents](#Contents)<br><br>

# Karnaugh Map
- 부울식을 단순화할 수 있는 체계적인 방법
- 대수적 방법으로도 부울식을 단순화 할 수 있지만, 식이 복잡해지면 단순화하기 어려움

<br>

## Gray Code
- 수의 크기가 변할 때 인접한 수 사이에 한 자리만 변하게 만들어진 코드
- 순차적인 진행에 유리, 연산에 불리
- I/O장치, A/D변환기, 하드디스크 등에 사용

| 10진코드 | 2진코드 | 그레이코드 |
|:---:|:---:|:---:|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

<br>

## 카르노 맵 그리기
1. 변수의 개수에 따라 2^n 칸을 갖는 테이블을 만든다.
2. 부울식 SOP, POS에 따라 테이블을 완성시킨다.
3. 규칙에 따라 그룹화한다.
규칙1) 출력이 1인 셀들을 크기는 최대로 하고, 개수는 최소로 하는 직사각형으로 그룹화한다.
규칙2) 단, 크기는 2,4,8,16 ... 처럼 2의 제곱수를 가져야한다.
규칙3) 규칙1,2를 만족시키면서 출력이 1인 모든 셀들을 그룹화해야한다.
4. 그룹을 논리식으로 표현한다.

<br>[Contents](#Contents)<br><br>

# Logic Circuit
- 논리값을 결정하는 연산회로
- 논리게이트 및 플립플롭으로 구성

#### 논리연산, 논리소자, 논리회로
- 논리연산 (logic operation)
  - 하나 이상의 논리값으로 부터 새로운 논리값을 얻는 연산
- 논리소자 (logic gate, logic element)
   - 기본 소자`(트랜지스터, 다이오드, 등등)`들을 조합하여 논리연산을 물리적으로 구현한 것
   - AND, OR, NAND ... 등 여러가지 게이트
- 논리회로 (logic circuit)
  - 논리값을 결정하는 연산회로, 논리소자 및 플립플롭으로 구성
  - 조합논리회로와 순차논리회로가 있음

<br>

## 논리회로의 종류
- 조합논리회로 (Combinational Logic Circuit)
  - 현재의 입력을 조합해서 출력이 결정되는 회로
  - 기억소자가 없음
  - 클럭을 사용하지 않음
  - [논리게이트](#Logic-Gate)만으로 구성
  - `adder, multiplexer, en/decoder, gates` 등이 있음
- 순차논리회로 (Sequential Logic Circuit)
  - 현재상태와 입력을 조합해서 다음상태와 출력을 결정하는 회로
  - `Latch, Flip-Flops, Register, Memory` 등의 소자를 사용하여 현재상태를 저장
  - 클럭을 사용하여 값을 저장
  - `counter, register, clock divider, FSM` 등이 있음

<br>[Contents](#Contents)<br><br>

# Combinational Logic Circuit
- 현재의 입력을 조합해서 출력이 결정되는 회로
- 기억소자가 없음
- 클럭을 사용하지 않음
- [논리게이트](#Logic-Gate)만으로 구성
- `adder, multiplexer, en/decoder, gates` 등이 있음

<br>

## Adder
- 두 오퍼랜드를 더하는 조합논리회로
- 반가산기와 전가산기가 있음

<br>

## Comparator
- 두 수의 크기에 따라 같다,크다,작다의 3가지 상태를 출력하는 조합논리회로이다.

<br>

## Decoder & Encoder
- 디코더는 n비트 이진코드를 2<sup>n</sup>개의 서로다른 출력으로 만들어주는 논리회로를 말한다. 
- 인코더는 디코더의 반대로, 개별적인 입력을 코드화해서 이진코드로 만들어주는 논리회로이다. 

<br>

## Multiplexer (Mux)
- 여러 개의 입력 중 하나를 선택하여 출력으로 내보내는 조합논리회로
- 일종의 `데이터 선택기` 
- 입력의 개수에 따라 2-to-1, 4-to-1, .. 등이 있음

<br>

## Demultiplexer (DeMux)
- 1개의 입력을 2<sup>n</sup>개의 출력선 중 하나로 내보내는 조합논리회로
- 일종의 `데이터 분배기`
- 출력선의 개수에 따라 1-to-2, 1-to-4, ..등이 있음

<br>

## Parity
- 패리티는 디지털 신호 전송 시 전송 데이터에 1비트를 추가로 더 보내어 수신측에서 오류를 체크할 수 있게 해주는 조합논리회로

<br>[Contents](#Contents)<br><br>

# Sequential Logic Circuit
  - 현재상태와 입력을 조합해서 다음상태와 출력을 결정하는 회로
  - `Latch, Flip-Flops, Register, Memory` 등의 소자를 사용하여 현재상태를 저장
  - 클럭을 사용하여 값을 저장
  - `counter, register, clock divider, FSM` 등이 있음

#### Latch, Flip-Flops, Register, Memory
- 순차회로는 저장소로 위 4개를 사용할 수 있음
- 래치는 쓰기가 어려워 잘 안쓰임
- 실질적으로 플립플롭이 많이 쓰임
- 플립플롭이 여러 개 모이면 레지스터가 됨
- 메모리를 대신 순차회로의 저장소로 사용가능, 하지만 순차회로의 저장소로 대부분은 플립플롭을 사용

<br>

## SR Latch
- S=0을 입력하면 Q=1을 출력 `(Set)`
- R=0을 입력하면 Q=0을 출력 `(Reset)`
- S=0,R=0은 허용하지 않음
- S=1,R=1은 기존값 유지
- S,R이 각각 0일때 활성화되므로 `active-low 신호`라고 함

#### SR Latch의 상태표 (x는 어떤값이든지 상관없다는 기호)
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|S R|Q<sub>p</sub> Q'<sub>p</sub>|Q<sub>n</sub> Q'<sub>n</sub>|Comments|
|0 0|x x|? ?|`Not allowed`|
|0 1|x x|1 0|set|
|1 0|x x|0 1|reset|
|1 1|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|no change|

<br>

## Gated SR Latch
- EN(enable)신호가 있는 SR 래치
- EN=0이면 기존값 유지
- EN=1이면 SR 입력값에 따라 변화
- S,R이 1일 때 활성화되므로 `active-high` 신호이다.

#### Gated SR Latch의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|EN S R|Q<sub>p</sub> Q'<sub>p</sub>|Q<sub>n</sub> Q'<sub>n</sub>|Comments|
|0 x x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|no change|
|1 0 0|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|no change|
|1 0 1|x x|x x|reset|
|1 1 0|x x|x x|set|
|1 1 1|x x|1 1|`Not allowed`|

<br>

## D Latch
- Gated SR Latch의 입력 하나를 인버터로 묶어서 허용되지 않는 값 입력으로 들어갈 수 없도록 만든 래치
- 일반적으로 가장 많이 사용되는 래치
- EN=1이면 입력D를 그대로 출력하므로 `transparent latch`라고도 함

#### D Latch의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|EN D|Q<sub>p</sub> Q'<sub>p</sub>|Q<sub>n</sub> Q'<sub>n</sub>|Comments|
|0 x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|no changes|
|1 0|x x|0 1|reset|
|1 1|x x|1 0|set|

<br>

# 플립플롭 개요
- clock 신호가 변화하는 시점(edge)에 맞추어 동작`(Edge-sensitive)`하는 논리회로
- 반면에, Latch는 clock 신호 값에 맞추어 동작`(level-sensitive)`
- 상승/하강 edge 중 동작하는 edge에 따라 rising edge triggered F/F, falling edge triggered F/F가 있음
- D F/F, 

#### 플립플롭 동작 특성
- Propagation delay time (전달 지연 시간) : clock edge로부터 값이 출력되기까지 걸리는 시간
- Setup time : clock edge 전 미리 데이터가 안정되어야하는 최소시간
- Hold time : clock edge 후 미리 데이터가 유지되고 있어야하는 최소시간 

#### 플립플롭의 상태표와 여기표
- 상태표(stable table)은 플립플롭의 상태를 보여줌
- 여기표(excitation table)은 플립플롭의 상태를 바꾸기 위한 입력값을 알려줌
- p는 현재상태, n은 다음상태

<br>

### D F/F
- C(clock)=0 또는 1이면, 기존값 유지
- C=0->1로 바뀌는 순간(rising edge))에 D값에 따라 출력이 결정

#### D F/F의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
| Clk D | Q<sub>p</sub> Q'<sub>p</sub> | Q<sub>n</sub> Q'<sub>n</sub> |
| ↑ 0 | x x | 0 1 | Reset |
| ↑ 1 | x x | 1 0 | Set |
| 0 x | Q<sub>0</sub> Q'<sub>0</sub> | Q<sub>0</sub> Q'<sub>0</sub> | No change |
| 1 x | Q<sub>0</sub> Q'<sub>0</sub> | Q<sub>0</sub> Q'<sub>0</sub> | No change |

#### Stable table (D F/F)
|d p|n|
|:---:|:---:|
|0 0|0|
|0 1|0|
|1 0|1|
|1 1|1|

#### Excitation table (D F/F)
|state change p->n|F/F input d|
|:---:|:---:|
|0 0|0|
|0 1|1|
|1 0|0|
|1 1|1|

#### State Eq
- `n=d`

<br>

### Edge-triggered D F/F
- `pulse transition detector`를 이용해서 아주 짧은 시간만 D Latch의 EN=1로 만들어 마치 플립플롭 같은 효과를 만들어 냄
- pulse transition detector + D Lath

<br>

### Master-Slave D F/F
- 2개의 D Latch를 사용하여 만든 플립플롭
- 앞의 두가지 D F/F와 동작이 같다.

<br>

### JK F/F
- 카운터를 만들때 유용한 플립플롭
- K=1이면, Q=0 (Reset)
- J=1이면, Q=1 (Set)
- J=0, K=0이면 원래값을 유지
- J=1, K=1이면 원래값을 반대로 바꾼다. `(Toggle)`

#### JK F/F의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|Clk J K|Q<sub>p</sub> Q'<sub>p</sub>| Q<sub>n</sub> Q'<sub>n</sub> |
|↑ 0 0|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|
|↑ 0 1|x x|0 1|Reset|
|↑ 1 0|x x|1 0|Set|
|↑ 1 1|Q<sub>0</sub> Q'<sub>0</sub>|Q'<sub>0</sub> Q<sub>0</sub>|Toggle|
|x x x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|

|j k p|n|comments|
|0 0 0|0|no change|
|0 0 1|1|no change|
|0 1 0|0|reset|
|0 1 1|0|reset|
|1 0 0|1|set|
|1 0 1|1|set|
|1 1 0|1|toggle|
|1 1 1|0|toggle|

#### Excitation Table
|state change p->n|F/F input j k|
|:---:|:---:|
|0 0|0 x|
|0 1|1 x|
|1 0|x 1|
|1 1|x 0|

#### State Eq
- `n = jp'+k'p` 

<br>

### T F/F
- JK F/F의 J와 K를 AND게이트로 연결하여 T를 입력으로 함

#### T F/F의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|Clk T|Q<sub>p</sub> Q'<sub>p</sub>| Q<sub>n</sub> Q'<sub>n</sub> |
|↑ 0|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|
|↑ 1|Q<sub>0</sub> Q'<sub>0</sub>|Q'<sub>0</sub> Q<sub>0</sub>|Toggle|
|x x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|

|t p|n|
|:---:|:---:|
|0 0|0|
|0 1|1|
|1 0|1|
|1 1|0|

#### Excitation table
|stable change p->n|F/F input t|
|:---:|:---:|
|0 0|0|
|0 1|1|
|1 0|1|
|1 1|0|

#### State Eq
- `n = t'p+tp' = t⊕p`

<br>

### 비동기 리셋 D F/F (D F/F with Async. Reset)
- 동기(Synchronous): 클럭신호에 맞추어 값이 변할 경우
- 비동기(Asynchronous): 클럭신호와 상관업싱 값이 변할 경우
- 즉, 클럭 엣지와 상관없이 리셋을 할 수 있는 D 플립플롭

#### 비동기 리셋 D F/F의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|Reset Clk D|Q<sub>p</sub> Q'<sub>p</sub>| Q<sub>n</sub> Q'<sub>n</sub> |
|0 x x|x x|0 1|Reset|
|1 ↑ 0|x x|0 1|Reset|
|1 ↑ 1|x x|1 0|Set|
|1 x x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|

<br>

### 비동기 셋/리셋 JK F/F (JK F/F with Async. Set and Reset)
- 클럭신호와 상관없이 셋,리셋을 할 수 있는 JK F/F
- 비동기 Set은 `preset`
- 비동기 Reset은 `clear`
- preset, clear 모두 0일때 active되는 `active-low` 신호

#### 비동기 셋/리셋 JK F/F의 상태표
|Input|Present State|Next State|Comments|
|:---:|:---:|:---:|:---:|
|preset clear Clk J K|Q<sub>p</sub> Q'<sub>p</sub>| Q<sub>n</sub> Q'<sub>n</sub> |
|0 0 x x x|x x|? ?|Not allowed|
|0 1 x x x|x x|1 0|set|
|1 0 x x x|x x|0 1|reset|
|1 1 ↑ 0 0|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|
|1 1 ↑ 0 1|x x|0 1|reset|
|1 1 ↑ 1 0|x x|1 0|set|
|1 1 ↑ 1 1|Q<sub>0</sub> Q'<sub>0</sub>|Q'<sub>0</sub> Q<sub>0</sub>|Toggle|
|1 1 x x x|Q<sub>0</sub> Q'<sub>0</sub>|Q<sub>0</sub> Q'<sub>0</sub>|No change|

<br>

## Reference
- [KOCW 강의 - 디지털 논리 회로 익히기](http://www.kocw.net/home/search/kemView.do?kemId=1319470)
- [정보통신기술용어해설](http://www.ktword.co.kr/abbr_view.php?nav=2&id=124&m_temp1=4893)
- [Wikipedia - floating point arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
- [Wikipedia - Logic Gate](https://en.wikipedia.org/wiki/Logic_gate)
- [Wikipedia - Verilog](https://en.wikipedia.org/wiki/Verilog)
- [Wikipedia - Bool Algebra](https://en.wikipedia.org/wiki/Bol_loop)


