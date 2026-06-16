# [순차 탐색] 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있을 때, 찾고자 하는 수가 있는지 판단한다.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_sequential(target, array):
    for number in array:
        if target == number:
            return True

    return False

result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True