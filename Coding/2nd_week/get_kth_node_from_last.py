# Q. 링크드 리스트의 끝에서 k번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(value)

    def get_kth_node_from_last_v1(self, k):
        length = 1
        current = self.head

        # 전체 링크드 리스트 길이 구하기
        while current.next is not None:
            current = current.next
            length += 1

        # 탐색 횟수
        end_length = length - k
        current = self.head

        for i in range(end_length):
            current = current.next

        return current

    def get_kth_node_from_last_v2(self, k):
        # 두 개의 포인터(slow, fast)로 탐색
        slow = self.head
        fast = self.head

        # fast 포인터 위치 잡기: 각 포인터는 k만큼 떨어진 채로 움직인다.
        # slow <-- k칸 --> fast
        for i in range(k):
            fast = fast.next

        # 두 포인터를 동시에 움직인다.
        # fast 포인터의 탐색이 종료되면 slow 포인터가 위치한 노드를 반환한다.
        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList("쿠리")
linked_list.append("쌀밥")
linked_list.append("두쫀쿠")
linked_list.append("햄햄")
linked_list.append("버블냥니")
linked_list.append("칫솔")
linked_list.append("쿠로미")
linked_list.append("디젤")
linked_list.append("버블티")
linked_list.append("라면")

print("ver.1 : ", linked_list.get_kth_node_from_last_v1(5).data)  # 칫솔
print("ver.2 : ", linked_list.get_kth_node_from_last_v2(4).data)  # 쿠로미