# 최빈값 찾기
# Q. 문자열을 입력 받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단, 최빈값을 가진 알파벳이 여러 개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오.)

#############################
# ** ver.1
#############################
def find_max_occurred_alphabet(text):
    alphabet_counts = [0] * 26

    for char in text:
        # 알파벳일 때만 빈도수 체크
        if not char.isalpha():
            continue
        alphabet_index = ord(char) - ord('a')
        alphabet_counts[alphabet_index] += 1

    max_count = alphabet_counts[0]
    most_frequent_alphabet = 'a'

    for alphabet_index in range(len(alphabet_counts)):
        count = alphabet_counts[alphabet_index]

        if count > max_count:
            max_count = count
            most_frequent_alphabet = chr(ord('a') + alphabet_index)

    return most_frequent_alphabet

ver1 = find_max_occurred_alphabet
print("정답 = e 현재 풀이 값 =", ver1("hello my name is haemhaem"))
print("정답 = g 현재 풀이 값 =", ver1("we love algggorithm"))
print("정답 = k 현재 풀이 값 =", ver1("best of best haemkkkkuri"))

#############################
# ver.2
#############################
def find_max_occurred_alphabet_v2(string):
    # 알파벳 배열을 만들고 시작
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # 기본값
    max_count = 0
    most_frequent_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        # 빈도수
        alphabet_counts = 0

        for char in string:
            if char == alphabet:
                alphabet_counts += 1

        if alphabet_counts > max_count:
            max_count = alphabet_counts
            most_frequent_alphabet = alphabet

    return most_frequent_alphabet

ver2 = find_max_occurred_alphabet_v2
print("정답 = e 현재 풀이 값 =", ver2("hello my name is haemhaem"))
print("정답 = g 현재 풀이 값 =", ver2("we love algggorithm"))
print("정답 = k 현재 풀이 값 =", ver2("best of best haemkkkkuri"))