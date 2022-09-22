class Node:
    def __init__(self, name, left=None, right=None): # 섬 생성자 
        self.name = name 
        self.left = left
        self.right = right

def map(): # 지도 만들기 
    n1 = Node('H')    # 11개의 섬 만들기 
    n2 = Node('F')
    n3 = Node('S')
    n4 = Node('U')
    n5 = Node('E')
    n6 = Node('Z')
    n7 = Node('K')
    n8 = Node('N')
    n9 = Node('A')
    n10 = Node('Y')
    n11 = Node('T')

    n1.left = n2   # 11개의 섬 교량을 잇기 
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right = n10
    n9.right = n11 

    return n1 




def A_course(n):  # A코스 
    if n != None:
        print(n.name, '-> ', end=' ') # 섬 n방문
        A_course(n.left) # n의 왼쪽으로 진행
        A_course(n.right) # n의 오른쪽으로 진행 

def B_course(n): # B 코스 
    if n != None:
        B_course(n.left)
        print(n.name, '-> ', end=' ') # 섬 n방문 
        B_course(n.right)

def C_course(n): # C 코스
    if n != None:
        C_course(n.left)
        C_course(n.right)
        print(n.name, '-> ', end=' ')


start = map() # 시작 섬을  n1으로

print('A-코스:\t', end="")
A_course(start)
print('\nB-코스:\t', end="")
B_course(start)
print('\nC-코스:\t', end="")
C_course(start)


