# 클래스(Node) 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 클래스(LinkedList) 정의
class LinkedList:
    def __init__(self, value):
        self.head = Node(value) # Linked List의 '시작하는 노드'를 만든다.

    # Linked List의 가장 마지막 노드에 새로운 노드를 연결한다.
    def append(self, value):
        # 1. 가장 마지막 노드를 찾는다.
        # 1) 시작 노드를 current로 지정
        current = self.head

        # 2) 가장 마지막 노드까지 탐색 -> next = None
        while current.next is not None:
            current = current.next  # current = 가장 마지막 노드

        # 2. 마지막 노드에 새로운 노드를 연결한다.
        current.next = Node(value)

    # Linked List의 모든 노드를 출력한다.
    def print_all(self):
        current = self.head

        while current is not None:  # 현재 노드가 존재하는 동안 반복
            print(current.data)
            current = current.next  # 기준을 다음 노드로 업데이트

# Linked List 생성
linked_list = LinkedList("쿠리")

# 노드 추가
linked_list.append("햄햄")
linked_list.append("버터떡")
linked_list.append("두쫀쿠")
linked_list.append("말차빙젤라또")
linked_list.append("쌀밥")

# 전체 노드 확인
linked_list.print_all()