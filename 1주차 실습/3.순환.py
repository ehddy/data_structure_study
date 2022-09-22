
def recurse(count):
    if count <= 0 :
        print('.')
    else:
        print(count, ' *')
        recurse(count-1)
    
recurse(5)

# 순환 방법을 통한 팩토리얼 계산 프로그램 
def factorial(n):
    if n <= 1:
        return 1 
    else:
        return n * factorial(n-1)

print(factorial(4))

# 반복문을 사용하여 팩토리얼 계산 

factorial = 1

for i in range(1, 5):
    factorial *= i

print(factorial)