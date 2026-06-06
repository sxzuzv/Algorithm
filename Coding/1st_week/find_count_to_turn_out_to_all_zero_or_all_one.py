# 문자열 뒤집기
# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# (뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.)
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 모든 수를 0으로 바꿔야 할 때, 최소 횟수
    count_to_all_zero = 0
    # 모든 수를 1로 바꿔야 할 때, 최소 횟수
    count_to_all_one = 0

    # 0번째 인덱스에 대한 계산을 포함
    # 0번째 인덱스의 값이 "0"인 경우, 모두 1로 변경하고자 할 때는
    # count_to_all_one += 1
    # 0번째 인덱스의 값이 "1"인 경우, 모두 0으로 변경하고자 할 때는
    # count_to_all_zero += 1
    if string[0] == "0":
        count_to_all_one += 1
    elif string[0] == "1":
        count_to_all_zero += 1

    # 0번째 인덱스부터 문자열 길이의 - 2만큼 반복문을 실행
    # 현재 인덱스와 현재 인덱스 + 1의 문자를 비교할 것이므로,
    # 문자열과 동일한 인덱스(문자열 길이 - 1)까지 순회하면 안 된다. (+ 1 위치의 문자가 없기 때문)
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == "0":
                # 0으로 변하는 순간 -> 여기서 문자를 뒤집으면 '1'
                count_to_all_one += 1
            if string[i + 1] == "1":
                # 0로 변하는 순간 -> 여기서 문자를 뒤집으면 '0'
                count_to_all_zero += 1

    print (count_to_all_zero, count_to_all_one)
    # 최소 횟수를 반환하면 되므로 min() 사용
    return min(count_to_all_zero, count_to_all_one)

result = find_count_to_turn_out_to_all_zero_or_all_one("011110")
print(result)