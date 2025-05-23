"""자연수를 입력받고 해당 자연수의 약수 중 소수인 숫자들만 반환하는 프로그램"""


def find_divisors(num):
    """입력받은 자연수의 약수들의 리스트를 반환"""
    divisors = []

    for i in range(1, int((num**0.5)) + 1):  # 입력받은 숫자의 제곱근+1까지 확인
        if num % i == 0:
            divisors.append(i)  # 작은 값을 추가
            if i != num // i:
                divisors.append(num // i)  # 짝이 되는 큰 값을 추가

    return divisors  # 약수들을 리스트 형태로 반환


def is_prime(num):
    """입력받은 자연수가 소수인지 판별하여 bool 형태로 반환"""
    if num < 2:  # 1은 소수가 아님
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True  # 소수인지 bool 형태로 반환


def find_prime_divisors(num):
    """입력받은 자연수의 약수들 중에서 소수들만 리스트로 반환"""

    return [
        i for i in find_divisors(num) if is_prime(i)
    ]  # 리스트 컴프리헨션을 사용해 더 간결하게 표현해봤음


print(find_prime_divisors(user_input := int(input("자연수를 입력하세요: "))))
