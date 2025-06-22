class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

def print_linked_list(head):
    # Correction to match example
    if not head:
        print("None")
        return
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    left = right = head
    
    # Mario (target) -> Peach -> Luigi -> Daisy -> None
    # None
    if target == 1 or head is None:
        return head
    
    for i in range(1, target-1):
        left = right
        right = right.next
        if right is None: # Target is out of bounds
            return head

    # left   right
    # Mario (target-1) -> Luigi (target) -> Daisy -> None
    if left == right:
        right = left.next              # Mario (left) -> Luigi (right) -> Daisy -> None
        left = right.next              # Mario (left) -> Daisy -> None
        right.next = left              # Luigi (right) -> Mario (left) -> Daisy -> None
    #          left         right
    # Wario -> Mario -> Peach (target-1) -> Luigi (target) -> None
    elif right.next.next is None:
        left.next = right.next         # Wario -> Mario (left) -> Luigi -> None
        left.next.next = right         # Wario -> Mario (left) -> Luigi -> Peach (right)
        right.next = None              # Wario -> Mario (left) -> Luigi -> Peach (right) -> None
    #          left          right    
    # Wario -> Mario -> Peach (target-1) -> Luigi (target) -> Daisy -> Bowser -> None
    else:
        left.next = right.next         # Wario -> Mario (left) -> Luigi -> Daisy -> Wario -> Bowser -> None
        right.next = left.next.next    # Peach (right) -> Daisy -> Wario -> Bowser -> None
        left.next.next = right         # Wario -> Mario (left) -> Luigi -> Peach (right) -> Daisy -> Wario -> Bowser -> None

    return head

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))
racers3 = Node("Mario", Node("Luigi", Node("Peach", Node("Daisy"))))
racers4 = Node("Mario")
racers5 = Node("Mario", Node("Peach"))
racers6 = Node("Mario", Node("Luigi", Node("Peach")))

print_linked_list(increment_rank(racers1, 3))   # Mario -> Luigi -> Peach -> Daisy
print_linked_list(increment_rank(racers2, 1))   # Mario -> Luigi
print_linked_list(increment_rank(None, 1))      # None
print_linked_list(increment_rank(racers3, 4))   # Mario -> Luigi -> Daisy -> Peach
print_linked_list(increment_rank(racers4, 1))   # Mario
print_linked_list(increment_rank(racers5, 2))   # Peach -> Mario
print_linked_list(increment_rank(racers6, 5))   # Mario -> Luigi -> Peach