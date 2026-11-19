N = int(input())
nums = list(map(int, input().split()))

nums.sort()

result = nums[1] - nums[0]

for i in range(1, N):
    val = nums[i] - nums[i - 1]

    if val < result:
        result = val

print(result)