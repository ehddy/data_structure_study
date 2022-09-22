class Node:
    def __init__(self, item):
        self.data = item
        self.next = None 

# 정렬된 단순연결리스트를 순서대로 병합 
class Solution: 
    def merge_sort_Lists(self, l1: Node, l2: Node):
            # 아무 값도 없는 dummy노드를 생성 
            current_node = Node(None) # (0, None)
            # dummy노드를 새로운 변수에 저장 
            return_node = current_node
        
            while l1 and l2:
                # 조건문을 통해 dummy노드(current_node)의 next에다 l1 or l2를 연걸 
                if l1.data < l2.data:
                    current_node.next = l1
                    l1 = l1.next
                    current_node = current_node.next
                else:
                    current_node.next = l2
                    l2 = l2.next
                    current_node = current_node.next
                # l1이나 l2 둘 중 하나라도 None이면 반복문을 중단 
            
            # l1이 None이면 l2를 리턴, 
            # l2이 None이면 l1를 리턴하여 cur_node에 저장 
            if l1:
                current_node.next = l1
            if l2:
                current_node.next = l2
            
            # 기존 dummy노드를 참조한 return_node의 next를 리턴 
            # 직접 실습을 할 때, data.next를 반복하여 병합된 리스트를 표현할 수 있음(밑에 구현 코드 실행)
            return return_node.next

l1 = Node(2)
l1.next = Node(3)
l1.next.next = Node(4)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(7)

# 중복된 값의 합을 프린트 하는 코드 
d = Solution()
lists = d.merge_sort_Lists(l1, l2)
while lists is not None:
    if lists.next == None:
        print(lists.data)
    else:
        print('{0} -> '.format(lists.data), end='')
    lists = lists.next


