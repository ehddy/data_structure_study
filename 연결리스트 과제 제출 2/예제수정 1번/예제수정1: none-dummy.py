# dummy 없는 이중 연결 리스트 
class NON_Dummy_DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link
    def __init__(self):
        self.size = 0
        self.head = None

    def size(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0
    
    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None, None)
        else:
            p = self.head
            self.head = self.Node(item, None, p)
            p.prev = self.head
        self.size += 1 
    
    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        t.next = n
        p.prev = n 
        self.size += 1


    def insert_after(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        t.next = n
        p.prev = n 
        self.size += 1

    def delect(self, x):
        f = x.prev 
        r = x.next
        f.next = r 
        r.prev = f 
        self.size -= 1 
        return x.item 
    
    def print_list(self):
        p = self.head
        print("head ->  ", end='')
        while p:
            if p.next != None:
                print(p.item, ' <-> ', end='')
            else:
                print(p.item)
            p = p.next
    # 탐색 메서드 추가 
    def search(self, target):
        p = self.head 
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None
    
class EmptyError(Exception):
    pass



# 예제 실행 코드 
d = NON_Dummy_DList()
d.insert_front('banana')
d.insert_front('apple')
d.insert_front('grape')
d.insert_after(d.head.next, 'orange')
print('banana의 위치는:', d.search('banana'))
d.print_list()


