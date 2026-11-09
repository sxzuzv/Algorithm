scores = list(map(int, input().split()))
count = [0] * 10

for i, score in enumerate(scores):
    if score == 0:
        break
    elif score < 10:
        continue
    else:
        count[score // 10 - 1] += 1

for i in range(10, 0, -1):
    print(f'{i*10} - {count[i-1]}')
