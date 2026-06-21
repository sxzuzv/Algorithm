# 더하거나 빼거나
# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
# -1+1+1+1+1 = 3 / +1-1+1+1+1 = 3 / +1+1-1+1+1 = 3 / +1+1+1-1+1 = 3 / +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열, 타겟 넘버가 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    return plus_or_minus_recursive(
        array,
        target,
        0,
        0
    )


def plus_or_minus_recursive(array, target, index, current_sum):
    if index == len(array):
        if target == current_sum:
            return 1
        return 0

    # 현재 숫자를 더하는 경우의 수
    plus = plus_or_minus_recursive(
        array,
        target,
        index + 1,
        current_sum + array[index]
    )

    # 현재 숫자를 빼는 경우의 수
    minus = plus_or_minus_recursive(
        array,
        target,
        index + 1,
        current_sum - array[index]
    )

    return plus + minus


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5