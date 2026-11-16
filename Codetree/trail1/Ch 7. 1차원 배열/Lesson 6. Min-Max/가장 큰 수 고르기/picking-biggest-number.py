numbers = list(map(int, input().split()))

max_num = numbers[0]

for num in numbers[1:]:
    if num > max_num:
        max_num = num

print(max_num)
