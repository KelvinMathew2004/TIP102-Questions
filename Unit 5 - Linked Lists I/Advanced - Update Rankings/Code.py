class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    # Correction to match sample
    if not head:
        print("None")
        return
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    previous = current = head
    
    if target == 1 or head is None:
        return head
    
    for i in range(1, target-1):
        previous = current
        current = current.next
        if current is None:
            return head
        
    if current.next.next is None:
        previous.next = current.next
        previous.next.next = current
        current.next = None
    else:
        previous.next = current.next
        current.next = previous.next.next
        previous.next.next = current

    return head

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1))