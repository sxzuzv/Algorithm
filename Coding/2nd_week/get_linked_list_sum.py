# 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
# (단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.)

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(value)

def linked_list_to_number(linked_list):
    number = 0
    current_node = linked_list.head

    while current_node is not None:
        number = number * 10 + current_node.data
        current_node = current_node.next

    return number

def get_linked_list_sum(linked_list_1, linked_list_2):
    number_1 = linked_list_to_number(linked_list_1)
    number_2 = linked_list_to_number(linked_list_2)

    return number_1 + number_2

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2)) # 678 + 354 = 1032