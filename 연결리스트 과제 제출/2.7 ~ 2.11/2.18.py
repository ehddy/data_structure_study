def split(L):
    a = []
    for i in range(len(L)):
        if L[i] not in a:
            a.append(L[i])
        else:
            return L[i]
        



# 실습 예제 코드 (바로 실행시키면 됩니다.)
L = [1, 2, 4, 6, 5, 6, 3, 9, 8] 

print('중복된 값:', split(L))

# 크기가 N(N > 3)인 파이썬 리스트에 1에서 N-1까지의 정수가 저장되어 있음, 그 중 2개에 중복값을 찾아야 한다.  
"""기존에는 count함수를 쓰면 쉽게 구할 수 있지만, 
 def split(L):
    for i in range(1, len(L)):
        if L.count(i) == 2:
            return i
n(1)의 메모리를 사용해야 해서 수정이 필요 
cont 대신 not in을 사용하여 중복된 값을 도출
"""