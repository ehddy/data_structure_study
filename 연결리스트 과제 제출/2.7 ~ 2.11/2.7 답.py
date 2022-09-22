from slist import SList

s1 = SList()
s1.insert_front(42)
s1.insert_front(27)
s1.insert_front(23)
s1.insert_front(15)
s1.insert_front(9)
s1.insert_front(5)
print('List 1: ', end='')
s1.print_list()

s2 = SList()
s2.insert_front(43)
s2.insert_front(26)
s2.insert_front(23)
s2.insert_front(14)
s2.insert_front(8)
s2.insert_front(4)
print('List 2: ', end='')
s2.print_list()

nodeS1 = s1.head
nodeS2 = s2.head
sum = 0

while (nodeS1 != None) and (nodeS2 != None):
    if nodeS1.item < nodeS2.item:
        nodeS1 = nodeS1.next 
    elif nodeS1.item > nodeS2.item:
        nodeS2 = nodeS2.next 
    else:
        sum += nodeS1.item
        sum += nodeS2.item

        nodeS1 = nodeS1.next
        nodeS2 = nodeS2.next 

print()
print('Sum:', sum)