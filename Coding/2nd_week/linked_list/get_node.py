# get_node(index) : N번째 index에 위치한 원소 찾기

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

    def print_all(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def get_node(self, index):
        current = self.head
        current_index = 0

        while current is not None and current_index != index:
            current = current.next
            current_index += 1

        if current is None:
            return None

        return current

linked_list = LinkedList("쿠리")
linked_list.append("버블냥")
linked_list.append("두쫀쿠")
linked_list.append("쿠리니니")
linked_list.append("버블냥니")

get_kurinini = linked_list.get_node(3)
print(get_kurinini.data) # 쿠리니니