# 최댓값 찾기
# Q. 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

def find_max_num(array):
    max_number = array[0]
    for number in array:
        if number > max_number:
            max_number = number
    return max_number

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 28 / 현재 풀이 값 = ", find_max_num([6, 1, 20, 21, 27, 28]))