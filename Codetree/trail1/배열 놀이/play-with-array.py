N, Q = map(int, input().split())
elements = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))

    # query[0] > 질의 종류 (1, 2, 3 중 1)
    kind = query[0]

    if kind == 1:
        print(elements[query[1] - 1])
    elif kind == 2:
        if query[1] in elements:
            print(elements.index(query[1]) + 1)
        else:
            print(0)
    else:
        s, e = query[1], query[2]
        print(*elements[s - 1:e])
