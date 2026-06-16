# 카운트다운
# 60에서 0까지 숫자를 출력하시오.

def count_down(number):
    print(number)

    if number - 1 < 0:
        return

    count_down(number - 1)

count_down(60)