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

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    a = sandwich_a.next
    b = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(a, b)

    return sandwich_a

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_a_2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a_2, sandwich_c))
# Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
# Bacon -> Bread -> Lettuce -> Tomato