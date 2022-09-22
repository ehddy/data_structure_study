from bst_5_21 import BST

if __name__ == '__main__':
    t = BST()
    t.put(70, '')
    t.put(30, '')
    t.put(80, '')
    t.put(10, '')
    t.put(50, '')
    t.put(40, '')
    print('삽입 전 전위순회:\t', end='')
    t.preorder(t.root)
    print('\n삽입 전 중위순회:\t', end='')
    t.inorder(t.root)

    t.put(60, '')
    print('\n\n삽입 후 전위순회:\t', end='')
    t.preorder(t.root)
    print('\n삽입 후 중위순회:\t', end='')
    t.inorder(t.root)