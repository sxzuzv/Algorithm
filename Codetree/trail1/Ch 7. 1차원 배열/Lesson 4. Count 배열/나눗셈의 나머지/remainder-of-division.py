A, B = map(int, input().split())
count = [0] * B  # A / B 나눗셈 연산 시 나머지는 0 ~ B-1 범위다.
result = 0

while A > 1:
    count[A % B] += 1
    A = A // B

print(sum(c ** 2 for c in count))