n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


isSubarray = False
for start in range(len(A) - len(B) + 1):  # A 끝을 넘지 않는 시작점만
    matched = True
    for j in range(len(B)):
        if A[start + j] != B[j]:
            matched = False
            break
    if matched:
        isSubarray = True
        break

print('Yes' if isSubarray else 'No')