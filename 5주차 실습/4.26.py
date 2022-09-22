from binary_tree_4_26 import BinaryTree, Node 
if __name__ == '__main__':
    t = BinaryTree()
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D') 
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')

    
    a.left = b
    a.right = c
    b.left = d
    d.right = g
    c.left = e
    c.right = f
    e.left = h
    e.right = i

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