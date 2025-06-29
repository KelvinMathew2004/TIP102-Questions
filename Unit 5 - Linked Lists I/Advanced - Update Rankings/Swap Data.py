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
    
    for i in range(1, target):
        left = right
        right = right.next
        if right is None: # Target is out of bounds
            return head

    temp = right.player_name
    right.player_name = left.player_name
    left.player_name = temp

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