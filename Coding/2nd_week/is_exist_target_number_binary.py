# 무작위 수 찾기
# 숫자로 이루어진 배열이 있을 때, 2가 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    sorted_array = sorted(array) # 오름차순한 새 배열 반환

    start = 0
    end = len(sorted_array) - 1

    while start <= end:
        mid = (start + end) // 2

        if sorted_array[mid] == target:
            return True

        elif target < sorted_array[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)