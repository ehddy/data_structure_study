def split(L, k):
    a = []
    b = []
    for i in L:
        if i <= k:
            a.append(i)
        else:
            b.append(i)
            

    return a + b

# 실습 예제 코드 (바로 실행시키면 됩니다.)
L = [4, 2, 6, 1, 8, 5, 7, 2]

print(split(L, 3))

# N개의 정수를 가진 파이썬 리스트 a의 원소들을 k와 같거나 작은 원소들을 왼쪽으로, 즉 a[0]으로 모아놓고, k보다 큰 원소들을 오른쪽으로 분리저장 
# for문이 한번(N번)만 실행했으며 그 안에 있는 append는 O(1)의 수행시간을 갖고 있으니 split 함수는 O(N)의 수행속도를 가졌다고 볼 수 있다.  