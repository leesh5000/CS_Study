#include <iostream>

/* Implementation of Queue using Array
 
 ***********************************
 *** Abstract Data Type in Queue ***
 ***********************************
 
 1. size_t Size() : 큐 사이즈 반환
 2. void Enqueue(T data) : 큐 데이터 추가 연산
 3. T Dequeue(T data) : 큐 데이터 삭제 연산
 
 */

template <typename T>
class Queue
{
private:
    size_t _front, _rear, _size, _cap;
    T* _arr;
    static const size_t Q_LEN = 8;
    
    bool IsFull() { return (_size == _cap - 1) ? true : false; }
    bool IsEmpty() { return (_size == 0) ? true : false; }
    
public:
    Queue(size_t cap = Q_LEN) : _front(0), _rear(0), _size(0), _cap(cap), _arr(new T[cap]) { } // cap의 초기값은 Q_LEN
    Queue(const Queue &q) : _front(q._front), _rear(q._rear), _size(q._size), _cap(q._cap)
    {
        for (int i=q._front; i<=q._rear; i++)
            _arr[i] = q._arr[i];
    }
    ~Queue() { delete[] _arr; }
  
    T& operator[](int i) { return _arr[i];}

    size_t Size() { return _size; }
    
    void Enqueue(T data)
    {
        if (IsFull()) return;
        
        _arr[_rear] = data;
        _rear = ++_rear % _cap;
        _size++;
        
        std::cout<<data<<" enqueue to queue\n";
    }
    
    T Dequeue()
    {
        if (IsEmpty()) return NULL;
        
        T rData = _arr[_front];
        _front = ++_front % _cap;
        _size--;
        
        std::cout<<rData<<" dequeue from queue\n";
        return rData;
    }
};

int main()
{
    /* 동적할당
     Queue<int>* q = new Queue<int>();
     q->Enqueue(10);
     */
    
    Queue<int> q;
    
    q.Enqueue(10);
    q.Enqueue(20);
    q.Enqueue(30);
    q.Enqueue(40);
    q.Enqueue(50);
    
    puts("\n--- while() Start ---");
    while(q.Size() != 0)
        q.Dequeue();
    
    return 0;
}

/* All Output
 
 10 enqueue to queue
 20 enqueue to queue
 30 enqueue to queue
 40 enqueue to queue
 50 enqueue to queue

 --- while() Start ---
 10 dequeue from queue
 20 dequeue from queue
 30 dequeue from queue
 40 dequeue from queue
 50 dequeue from queue
 
 */

