from binary_tree_4_23 import BinaryTree, Node 
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

    # 왼쪽 자식 - 오른쪽 형제 표현은 노드의 차수가 일정하지 않은 일반적인 트리를 구현하는 데 매우 효율 
    # 노드의 왼쪽 자식과 왼쪽 자식의 오른쪽 형제노드를 가리키는 2개의 레퍼런스만을 사용 
    # 왼쪽자식 - 오른쪽형제 표현의 트리 
    a.left = b
    b.left = e
    e.right = f 
    b.right = c
    c.left = g
    g.right = h
    h.right = i
    i.right = j
    c.right = d
    d.left = k
    k.right = l
    l.right = m
    t.root = a 



# 실습 예제 코드 (바로 실행시키면 됩니다.) 
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n후위순회:\t', end='')
    t.postorder(t.root)
    print('\n레벨순회:\t', end='')
    t.levelorder(t.root)

