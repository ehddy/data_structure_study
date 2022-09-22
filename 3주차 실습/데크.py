from collections import deque
dq = deque('data')
for elem in dq:
    print(elem.upper(), end='')
print()
dq.append('r')
dq.appendleft('k')

print(dq)

dq.pop()
dq.popleft()

print(dq[-1])
print('x' in dq)
dq.extend('structure') # 맨 뒤와 맨 앞에 여러 항목 삽입 
dq.extendleft(reversed('python'))
print(dq)

a = reversed('python')
print(list(a))