N = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

print(f'{numbers[0]} {numbers[1]}')
