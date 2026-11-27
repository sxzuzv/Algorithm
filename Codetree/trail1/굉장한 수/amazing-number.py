# 홀수이면서 3의 배수 / 짝수이면서 5의 배수
N = int(input())

if (N % 2 != 0 and N % 3 == 0) or (N % 2 == 0 and N % 5 == 0):
    print('true')
else:
    print('false')