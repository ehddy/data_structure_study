class SList:
    class Node:
        # 노드 생성자: 항목과 다음 노드 레퍼런스
        def __init__(self, item, link):
            self.item = item        
            self.next = link 
   # 단순연결리스트 생성자: head와 항목 수(size)로 구성  
    def __init__(self):
        self.head = None
        self.size = 0


    def size(self):
            return self.size
        
    def is_empty(self):
            return self.size == 0  

    def insert_front(self, item):
        # empty인 경우 
        if self.is_empty():
            self.head = self.Node(item, None)
        # head가 새 노드 참조 
        else:
            self.head = self.Node(item, self.head)
        self.size += 1 

    def insert_after(self, item, p):
        # 새 노드가 p 다음 노드가 됨
        p.next = self.Node(item, p.next)
        self.size += 1
    
    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            # head가 둘째 노드를 참조 
            self.head = self.head.next
            self.size -= 1
    
    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next
        # p 다음 노드를 건너뛰어 연결 
        p.next = t.next
        self.size -= 1 

    def search(self, target):
        # head로부터 순차탐색 
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            
            p = p.next

    # underflow시 에러 처리 
class EmptyError(Exception):
    pass 

