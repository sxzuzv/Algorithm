# 배달 가능 여부
# Q. 주문 가능 메뉴와 유저의 주문 메뉴를 보고 현재 주문 가능 상태인지 여부를 반환하시오.

shop_menus = ["시오니니", "쿠리니니", "버블냥니", "댕트리니", "룐룐니니", "팡팡니니"]
shop_orders = ["쿠리니니", "댕트리니", "버블냥니"]


#############################
# ver.1 - 이진 탐색
#############################
def is_available_to_order(menus, orders):
    menus.sort()    # ['댕트리니', '룐룐니니', '버블냥니', '시오니니', '쿠리니니', '팡팡니니']

    for order in orders:
        if not is_exist_target_number_binary(order, menus):
            return False

    return True


def is_exist_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1

    while current_min <= current_max:
        current_guess = (current_min + current_max) // 2

        if target == array[current_guess]:
            return True

        elif target < array[current_guess]:
            current_max = current_guess - 1

        else:
            current_min = current_guess + 1

    return False


#############################
# ver.2 - set
#############################
def is_available_to_order_set(menus, orders):
    menus_set = set(menus) # 중복 제거된 menus

    for order in orders:
        if order not in menus_set:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
result_v2 = is_available_to_order_set(shop_menus, shop_orders)
print("ver.1 : ", result)
print("ver.2 : ", result_v2)