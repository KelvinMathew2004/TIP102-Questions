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

def is_mirrored(head):
    flipped = None
    fast = head
    slow = head
    
    while fast and fast.next:
        temp = Node(slow.value, flipped)
        flipped = temp
        
        slow = slow.next
        fast = fast.next.next

        if fast:                 # When odd A -> B -> C -> B -> A
            slow = slow.next     #                    s         f
                         

    curr = flipped

    while curr:
        if curr.value != slow.value:
            return False
        curr = curr.next
        slow = slow.next
    
    return True
    

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1))
# True
print(is_mirrored(list2))
# False