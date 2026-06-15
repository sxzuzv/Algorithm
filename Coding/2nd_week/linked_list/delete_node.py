# delete_node(index) : N번째 index의 원소 삭제

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

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            prev_node = self.get_node(index - 1)

            if prev_node is None:
                return None

            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_node(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
        else:
            # 삭제할 노드의 '이전' 노드만 알면 된다.
            prev_node = self.get_node(index - 1)

            if prev_node is None or prev_node.next is None:
                return

            prev_node.next = prev_node.next.next # 삭제 노드의 '다음 노드'를 연결!

linked_list = LinkedList("쿠리")
linked_list.append("버블냥")
linked_list.append("두쫀쿠")
linked_list.append("쿠리니니")
linked_list.append("버블냥니")

linked_list.delete_node(0) # [버블냥] -> [두쫀쿠] -> [쿠리니니] -> [버블냥니]
linked_list.delete_node(3) # [버블냥] -> [두쫀쿠] -> [쿠리니니]
linked_list.print_all()