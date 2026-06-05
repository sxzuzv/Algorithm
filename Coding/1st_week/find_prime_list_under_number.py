# 소수 나열하기
# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# (소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.)

#############################
# ver.1
#############################
def find_prime_list_under_number_v1(number):
    prime_list = []

    # 2부터 N까지 반복 필요, range(2, number + 1)
    for element in range(2, number + 1):
        for i in range(2, element):
            if element % i == 0:
                break
        else:
            prime_list.append(element)

    return prime_list

result = find_prime_list_under_number_v1(20)
print(result)

#############################
# ver.2
#############################
def find_prime_list_under_number_v2(number):
    prime_list = []

    for element in range(2, number + 1):
        # element 보다 작은 '소수'에 대해서만 나머지 연산
        # element 보다 작은 수 중 '소수'인 것은 prime_list에 저장 중
        for prime in prime_list:
            if element % prime == 0:
                break
        else:
            prime_list.append(element)

    return prime_list

result = find_prime_list_under_number_v2(20)
print(result)

#############################
# ver.3
#############################
def find_prime_list_under_number_v3(number):
    prime_list = []

    for element in range(2, number + 1):
        # N의 제곱근보다 크지 않은 어떤 소수로도 나눠 떨어지지 않는다.
        # 검사 대상 소수² <= N 이 성립하는 소수에 대해서만 나머지 연산을 진행한다.
        for prime in prime_list:
            if prime * prime <= element and element % prime == 0:
                break
        else:
            prime_list.append(element)

    return prime_list

result = find_prime_list_under_number_v3(20)
print(result)

#############################
# ver.4
#############################
def find_prime_list_under_number_v4(number):
    prime_list = []

    for element in range(2, number + 1):
        # N의 제곱근보다 크지 않은 어떤 소수로도 나눠 떨어지지 않는다.
        # 검사 대상 소수² <= N 이 성립하는 소수에 대해서만 나머지 연산을 진행한다.

        # 실제 반복 횟수를 최적화한다. -> 상태 변수 활용
        is_prime = True

        for prime in prime_list:
            # 나머지 연산이 필요 없다.
            if prime * prime > element:
                break

            if element % prime == 0:
                is_prime = False
                break

        # 나누어떨어지지 않았다면 소수로 판단한다.
        if is_prime:
            prime_list.append(element)

    return prime_list

result = find_prime_list_under_number_v4(20)
print(result)