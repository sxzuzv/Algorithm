# [이진 탐색] 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있을 때, 찾고자 하는 수가 있는지 판단한다.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    start = 0            # 시작 인덱스
    end = len(array) - 1 # 마지막 인덱스

    while start <= end:  # 시작 인덱스와 마지막 인덱스가 동일할 때까지 탐색
        mid = (start + end) // 2 # 중간 인덱스

        if target == array[mid]: # 찾는 수 == 배열의 중간 값
            return True

        elif target < array[mid]: # 찾는 수 < 배열의 중간 값 -> 우측 배열 값 탐색 고려 X
            # 좌측 기준으로 범위 줄여 이진 탐색
            end = mid - 1 # 중간 인덱스보다 작은 값(-1)을 범위의 마지막 인덱스로 설정

        else: # 찾는 수 > 배열의 중간 값 -> 좌측 배열 값 탐색 고려 X
            # 우측 기준으로 범위 줄여 이진 탐색
            start = mid + 1 # 중간 인덱스보다 큰 값(+1)을 범위의 시작 인덱스로 설정

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)  # True