N = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]
min_val_count = 1

for num in numbers[1:]:
    if num < min_val:     # 더 작은 값 발견 → 최솟값 바꾸고 개수 리셋
        min_val = num
        min_val_count = 1
    elif num == min_val:  # 현재 최솟값이랑 같음 → 개수만 +1
        min_val_count += 1

print(min_val, min_val_count)
