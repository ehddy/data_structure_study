from bst_5_22 import BST

if __name__ == '__main__':
    # right 방향으로 나열 
    t = BST()
    t.put(10, '')
    t.put(20, '')
    t.put(30, '')
    t.put(40, '')
    t.put(50, '')
    t.put(60, '')
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)

    # 거꾸로 삽입 # left 방향으로 존재 
    t_reverse = BST()
    t_reverse.put(60, '')
    t_reverse.put(50, '')
    t_reverse.put(40, '')
    t_reverse.put(30, '')
    t_reverse.put(20, '')
    t_reverse.put(10, '')
    print('\n전위순회:\t', end='')
    t_reverse.preorder(t.root)
    print('\n중위순회:\t', end='')
    t_reverse.inorder(t.root)