Y = int(input())

# 윤년 = 4로 나누어떨어지는데, 100으로는 안 나누어떨어지거나, 400으로 나누어떨어지는 해
if (Y % 4 == 0) and (Y % 100 != 0 or Y % 400 == 0):
    print('true')
else:
    print('false')