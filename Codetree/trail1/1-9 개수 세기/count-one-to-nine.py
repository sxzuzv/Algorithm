N = int(input())
arr = list(map(int, input().split()))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(arr)):
    count[arr[i] - 1] += 1

print(*count, sep='\n')