from 단순연결리스트stack import print_stack


def add(item): # 삽입 연산
    q.append(item)

def remove(): # 시간소요로 큐를 파이썬으로 쓴느 건 효율 x 
    if len(q) != 0:
        item = q.pop(0)
        return item

def print_q(): # 큐 출력 
    print('front -> ', end='')
    for i in range(len(q)):
        print('{!s:<8}'.format(q[i]), end='')
    print('  <-rear')

q = []
add('apple')
add('orange')
add('cherry')
print('사과 오렌지, 체리 삽입 후:\t', end='')
print_q()
remove()
print('remove한 후:\t\t', end='')
print_q()
remove()
print('remove한 후:\t\t', end='')
print_q()
add('grape')
print('포도 삽입 후:\t\t', end='')
print_q()
