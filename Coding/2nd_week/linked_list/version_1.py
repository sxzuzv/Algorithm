# 클래스(Node) 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 노드 생성
first_node = Node(6)
second_node = Node(28)

# 노드간 연결
first_node.next = second_node