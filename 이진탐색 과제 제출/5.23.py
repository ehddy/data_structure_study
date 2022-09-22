from bst_5_23 import BST

if __name__ == '__main__':
    t = BST()
    t.put(40, '')
    t.put(15, '')
    t.put(10, '')
    t.put(30, '')
    t.put(20, '')
    t.put(90, '')
    t.put(70, '')
    t.put(50, '')
    t.put(60, '')
    t.put(65, '')
    t.put(80, '')
    t.put(95, '')

    print('삭제 전 전위순회:\t', end='')
    t.preorder(t.root)
    print('\n삭제 전 중위순회:\t', end='')
    t.inorder(t.root)
    t.delete(40)
 
    print('\n\n삭제 후 전위순회:\t', end='')
    t.preorder(t.root)
    print('\n삭제 후 중위순회:\t', end='')
    t.inorder(t.root)

