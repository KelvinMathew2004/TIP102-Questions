class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while head_a or head_b:
        head_a_value = head_a.value if head_a else 0
        head_b_value = head_b.value if head_b else 0

        total = head_a_value + head_b_value + carry
        digit = total % 10
        carry = total // 10

        curr.next = Node(digit)
        curr = curr.next

        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next

    return dummy.next


head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))
# 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

