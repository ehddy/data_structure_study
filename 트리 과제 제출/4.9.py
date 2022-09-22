from binary_tree_4_9 import BinaryTree, Node 
if __name__ == '__main__':
    t = BinaryTree()
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D') # 16개의 노드 생성 
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    j = Node('J')
    k = Node('K')
    l = Node('L')
    m = Node('M')
    n = Node('N')
    o = Node('O')
    p = Node('P')

    
    a.left = b
    a.right = d
    b.left = e
    b.right = f
    e.left = j
    e.right = k
    k.left = n
    k.right = p
    p.left = o
    d.left = g
    d.right = i
    g.left = l
    g.right = m
    l.left = c
    i.left = h 

    t.root = a
# 실습 예제 코드 (바로 실행시키면 됩니다.)
    print('트리 높이 =', t.height(t.root))
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n후위순회:\t', end='')
    t.postorder(t.root)
    print('\n레벨순회:\t', end='')
    t.levelorder(t.root)