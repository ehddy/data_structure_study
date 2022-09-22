class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def _resize(self, n):
        old = self._data
        self._data = [None] * n
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

## https://wisdom-and-record.tistory.com/6 참고하자 

""" 단순연결리스트의 큐에서는 rear 에서 삽입하고 앞(front)에서 삭제연산을 해야 N(1)의 수행시간을 갖을 수 있다.
그 이유를 설명하기 전에  우선 큐는 가장 먼저 들어온 데이터를 가리키는 front 변수와 가장 나중에 들어온 데이터의 위치를 가리키는 
back 변수가 필요하다.
처음에는 큐가 비어있으므로 front와 rear 둘다 첫번 째 인덱스 0을 가리키고 있지만 값이 하나하나 추가되고 삭제가 되면 rear가 가리켜야 할 공간이 변한다. 
그러기 위해서는 인덱스를 조정하고 공간의 크기를 늘려야 되는데 그러기에는 메모리 낭비와 수행시간이 늘어난다.
그래서 만약 원형리스트의 큐를 구현하려면 rear의 인덱스를 증가시킬 때 단순히 1를 더하는 게 아니라 1를 더한 값에 전체 크기를 나눈 나머지를 할당한다.
그렇다면 rear 에서 삽입하고 앞(front)에서 삭제연산을 해야만 N(1)의 수행시간을 갖는 것이 아니라, 이전 노드의 레퍼런스나 첫 노드 둘 중 어디서든지 N(1)의 수행속도로 삽입과 삭제가 가능하다  """