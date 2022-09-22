def X(n):
    if n == 1: # n이 1일 경우 1를 리턴하여 X(1) = 1를 충족 
        return 1 
    else:
        return X(n-1) + (2 * n) -1    # 전 값들을 하나씩 참조하여 값을 도출 # n ** 2 형태의 제곱값을 반환해주는 알고리즘 


# print("X(1): ", X(1))
# print("X(2): ", X(2))
# print("X(3): ", X(3))
# print("X(4): ", X(4))
print("X(9): ", X(10))  