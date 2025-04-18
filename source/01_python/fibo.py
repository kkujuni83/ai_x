# fibo.py

def fibonacci_print(n):
    """n 미만의 피보나치 수열을 출력하는 함수"""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fibonacci_return(n):
    """n 미만의 피보나치 수열을 리스트로 반환하는 함수"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
