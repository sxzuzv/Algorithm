dice = list(map(int, input().split()))
count = [0] * 6

for die in dice:
    count[die - 1] += 1

for num, cnt in enumerate(count, 1):
    print(f'{num} - {cnt}')
    