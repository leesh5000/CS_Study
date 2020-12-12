import queue

# FIFO 큐
q = queue.Queue()
q.put("fun-coding")
q.put(10)
q.put(12.4)
q.put(True)

while q.qsize() != 0:
    print(q.get())

# LIFO 큐
q1 = queue.LifoQueue()
q1.put("fun-coding")
q1.put(10)
q1.put(12.4)
q1.put(True)

while q1.qsize() != 0:
    print(q1.get())

# Priority Queue
q2 = queue.PriorityQueue()
q2.put((4, "fun-coding"))
q2.put((3, 10))
q2.put((2, 12.4))
q2.put((1, True))

while q2.qsize() != 0:
    print(q2.get())

## 큐 구현 연습
my_q = list()

def enqueue(data):
    my_q.append(data)

def dequeue():
    data = my_q[0]
    del my_q[0]
    return data

    