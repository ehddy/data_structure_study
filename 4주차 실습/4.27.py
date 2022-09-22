from binary_tree_4_27 import BinaryTree, Node 
if __name__ == '__main__':
    t = BinaryTree()

    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400) # 8개의 노드 생성 
    n5 = Node(500)
    n6 = Node(600)
    n7 = Node(700)
    n8 = Node(800)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6    # 트리높이 및 4가지 트리 순회 
    n3.right = n7
    n4.left = n8 
    t.root = n1 

    print('target의 트리 높이 =', t.height(t.root))
    print('target의 전위순회:\t', end='')
    t.preorder(t.root)
    print('\ntarget의 중위순회:\t', end='')
    t.inorder(t.root)
    print('\ntarget의 후위순회:\t', end='')
    t.postorder(t.root)
    print('\ntarget의 레벨순회:\t', end='')
    t.levelorder(t.root)
    print(end='\n------------------------------------\n')



    
    # BinaryTree에 주어진 이진트리를 복사 
    a = t.mirror_copy()

    # 복사한 트리의 root를 복사대상 트리의 root와 동일하게 설정 
    a.root = t.root

    # 복사한 트리의 정보 출력 
    print('복사본 mirror의 트리 높이 =', t.height(a.root))
    print('복사본 mirror 트리의 전위순회:\t', end='')
    t.preorder(a.root)
    print('\n복사본 mirror 트리의 중위순회:\t', end='')
    t.inorder(a.root)
    print('\n복사본 mirror 트리의 후위순회:\t', end='')
    t.postorder(a.root)
    print('\n복사본 mirror 트리의 레벨순회:\t', end='')
    t.levelorder(a.root)

