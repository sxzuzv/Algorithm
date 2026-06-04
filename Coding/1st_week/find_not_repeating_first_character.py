# 반복되지 않는 문자
# 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# 첫 번째 문자의 기준은 ** 입력된 문자열에서의 등장 순서 **

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        index = ord(char) - ord("a")
        alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array

#############################
# ver.1
#############################
def find_not_repeating_first_character_v1(string):
    occurrence_array = find_alphabet_occurrence_array(string)

    for char in string:
        index = ord(char) - ord("a")

        if occurrence_array[index] == 0 or occurrence_array[index] > 1:
            continue

        if occurrence_array[index] == 1:
            first_character = chr(ord("a") + index)
            return first_character

    return '_'

result_v1 = find_not_repeating_first_character_v1
print("정답 = d 현재 풀이 값 =", result_v1("abadabac"))
print("정답 = c 현재 풀이 값 =", result_v1("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result_v1("aaaaaaaa"))

#############################
# ver.2
#############################
def find_not_repeating_first_character_v2(string):
    occurrence_array = find_alphabet_occurrence_array(string)
    not_repeating_character_array = []

    # 빈도수가 1인 알파벳만 뽑기
    for index in range(len(occurrence_array)):
        if occurrence_array[index] == 1:
            # 배열에 알파벳 넣기
            not_repeating_character_array.append(chr(ord("a") + index))

    for char in string:
        # 배열 안에 알파벳이 존재하는가?
        if char in not_repeating_character_array:
            return char

    return '_'

result_v2 = find_not_repeating_first_character_v2
print("정답 = d 현재 풀이 값 =", result_v2("abadabac"))
print("정답 = c 현재 풀이 값 =", result_v2("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result_v2("aaaaaaaa"))