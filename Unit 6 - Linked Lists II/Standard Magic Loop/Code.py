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

def loop_start(path_start):
    slow = fast = curr = path_start

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            while curr != slow:
                curr = curr.next
                slow = slow.next
            return curr.value

    return None


path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))
# Troll's Bridge