numbers = list(map(int, input().split()))
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
result = []

for i, num in enumerate(numbers):
    if num == 0:
        break
    elif num < 10:
        continue
    else:
        count[num // 10 - 1] += 1

for i in range(len(count)):
    print(f'{i+1} - {count[i]}')
