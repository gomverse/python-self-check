# 팩토리얼 찾기

num = 10


def find_factorial(num):
    if num == 0:
        return 1

    return num * find_factorial(num - 1)


print(find_factorial(num))

""" 작동 순서
find_factorial(10)
10 * find_factorial(9)
9 * find_factorial(8)
8 * find_factorial(7)
7 * find_factorial(6)
6 * find_factorial(5)
5 * find_factorial(4)
4 * find_factorial(3)
3 * find_factorial(2)
2 * find_factorial(1)
1 * find_factorial(0)
find_factorial(0)에서 return: 1
1 * 1 = return: 1
2 * 1 = return: 2
3 * 2 = return: 6
4 * 6 = return: 24
5 * 24 = return: 120
6 * 120 = return: 720
7 * 720 = return: 5040
8 * 5040 = return: 40320
9 * 40320 = return: 362880
10 * 362880 = return: 3628800
"""

# 피보나치 수열


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# 0번 ~ 10번째 피보나치 수 출력
for n in range(0, 11):
    print(fibonacci(n), end=" ")


# 재귀를 이용한 입력받은 숫자의 자리수 합치기


def add_digits(num: int) -> int:
    if int(num) < 10:
        return num

    print(num)
    return add_digits(sum([int(x) for x in str(num)]))


print(add_digits(13567))
