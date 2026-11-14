N = int(input())
numbers = list(map(int, input().split()))

count = 0

for i, num in enumerate(numbers):
    if int(num) == 2:
        count += 1

    if count == 3:
        print(i + 1)
        break
