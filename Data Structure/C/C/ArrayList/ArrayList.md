#  ArrayList

List는 ArrayList (배열리스트) 와 LinkedList (연결리스트) 두 가지가 있다.
ArrayList = 순차리스트 = 배열리스트 = 동적배열 = Vector ( C++ ) = List ( C# )
LinkedList = 연결리스트 = List ( C++ ) = LinkedList ( C# )
배열리스트는 데이터를 나란히 저장하고 중복된 데이터를 허용한다.

- 인터페이스
1. void Init (ArrayList* arrayList) : 리스트 초기화 함수
2. void Add (ArrayList* arrayList, Data data) : 리스트의 맨 끝에 데이터 추가
3. bool Insert (ArrayList* arrayList, Data data, int index) : 리스트의 중간에 데이터 삽입
4. Data Remove (ArrayList* arrayList) : 리스트 끝에 있는 데이터 삭제
5. void Clear (ArrayList* arrayList) : 리스트 메모리 해제
 
