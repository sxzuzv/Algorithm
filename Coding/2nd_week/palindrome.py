# 회문 검사
# Q. 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

def is_palindrome(string):
    n = len(string)

    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False

    return True

print(is_palindrome("abcba"))

#############################
# 재귀를 이용한 회문 검사 ver.1
#############################
def is_palindrome_recursive(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome_recursive(string[1:-1])

print(is_palindrome_recursive("abcba"))

#############################
# 재귀를 이용한 회문 검사 ver.2
#############################
def is_palindrome_recursive_v2(string, left, right):
    if left >= right:
        return True

    if string[left] != string[right]:
        return False

    return is_palindrome_recursive_v2(string, left + 1, right - 1)

input = "abcba"
print(is_palindrome_recursive_v2(input, 0, len(input) - 1))