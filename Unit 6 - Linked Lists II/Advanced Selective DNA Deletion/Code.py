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

def edit_dna_sequence(dna_strand, m, n):
    counter1 = 1
    counter2 = 0
    deletion = False
    curr = dna_strand

    while curr and curr.next:
        if not deletion:
            curr = curr.next
            counter1 += 1
            if counter1 == m:
                counter1 = 0
                deletion = True
        else:
            curr.next = curr.next.next
            counter2 += 1
            if counter2 == n:
                counter2 = 0
                deletion = False
    
    return dna_strand

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
# 1 -> 2 -> 6 -> 7 -> 11 -> 12
