from binary_tree_4_18 import BinaryTree, Node 
if __name__ == '__main__':
    t = BinaryTree()
    
    # 동일한 값을 가진 트리 두개 생성 
    # 1 
    a1 = Node('a')
    b1 = Node('b')
    c1 = Node('c')
    d1 = Node('d') # 8개의 노드 생성 
    e1 = Node('e')
    f1 = Node('f')
    g1 = Node('g')
    h1 = Node('h')
    
    a1.left = b1
    a1.right = c1
    b1.left = d1
    b1.right = e1
    c1.left = f1    # 트리높이 및 4가지 트리 순회 
    c1.right = g1
    g1.left = h1 
    t.root = a1 

    # 2 
    a2 = Node('a')
    b2 = Node('b')
    c2 = Node('c')
    d2 = Node('d') # 8개의 노드 생성 
    e2 = Node('e')
    f2 = Node('f')
    g2 = Node('g')
    h2 = Node('h')

    a2.left = b2
    a2.right = c2
    b2.left = d2
    b2.right = e2
    c2.left = f2    # 트리높이 및 4가지 트리 순회 
    c2.right = g2
    g2.left = h2 
    t.root = a2 

    # 이진 트리의 동일성 유뮤 확인(동일하면 True, 불일치하면 False를 리턴)
    print(t.q(a1, a2))
