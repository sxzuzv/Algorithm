numbers = list(map(int, input().split()))

# 범위 밖 값으로 초기화
max_val = -1000
min_val = 1000

for num in numbers:
    if num in (999, -999):
        break
    
    max_val = max(max_val, num)
    min_val = min(min_val, num)

print(f'{max_val} {min_val}')
