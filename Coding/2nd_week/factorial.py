# 팩토리얼
# factorial(n) = factorial(n) * factorial(n-1)
# factorial(n-1) = factorial(n-1) * factorial(n-2)

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))