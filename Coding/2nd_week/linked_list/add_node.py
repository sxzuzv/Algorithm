# add_node(index, value) : N번째 index에 원소(value) 추가

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
        # 추가할 신규 노드
        new_node = Node(value)

        # 추가할 index가 0번째인 경우 -> head 노드를 신규 노드로 교체
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            # 추가할 index의 '이전' 노드의 정보가 필요 -> index - 1 위치의 노드
            prev_node = self.get_node(index - 1)

            if prev_node is None:
                return None

            new_node.next = prev_node.next
            prev_node.next = new_node

linked_list = LinkedList("쿠리")
linked_list.append("버블냥")
linked_list.append("두쫀쿠")
linked_list.append("쿠리니니")
linked_list.append("버블냥니")

linked_list.add_node(2, "버터떡")
linked_list.add_node(5, "댕트리니")
linked_list.print_all()