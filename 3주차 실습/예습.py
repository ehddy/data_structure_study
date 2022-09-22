# 이중 연결 리스트
class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0
    
    def insert_before(self, p, t):
        t = p.prew
        n = self.Node(item, t, p)
        t.next = n
        p.prew = n 
        self.size += 1

    def insert_after(self, p, t):
        t = p.next 
        n = self.Node(item, p, t)
        p.next = n
        t.prew = n 
        self.size += 1

    def delect(self, x):
        f = x.prew 
        r = x.next
        f.next = r 
        r.prew = f 
        self.size -= 1 
        return x.item 
    
    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next 
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next 
class EmptyError(Exception):
    pass


# 원형연결리스트 
class Clist:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link 
    
    def __init__(self):
        self.last = None
        self.size = 0
    
    def no_items(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0

    
    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n 
        else:
            n.next = self.last.next
            self.last.next = n 
        self.size += 1
    
    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item 

    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next 
        self.size -= 1
        return x.item
    
    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            f = self.last.next
            p = f 
            while p.next != f:
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)
class EmptyError(Exception):
    pass