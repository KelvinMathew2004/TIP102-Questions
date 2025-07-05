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

def sort_list(head):
	tempNode = Node(float('-inf'), head)
	sortedEnd = tempNode
	
	while sortedEnd and sortedEnd.next:
		temp = sortedEnd.next
		sortedEnd.next = sortedEnd.next.next
		curr = tempNode
		
		while curr != sortedEnd and curr.next.value < temp.value:
			curr = curr.next
			
		temp.next = curr.next
		curr.next = temp
		
		if curr is sortedEnd:
			sortedEnd = temp
			
	return tempNode.next

head1 = Node(4, Node(2, Node(1, Node(3))))
head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))

print_linked_list(sort_list(head1))
print_linked_list(sort_list(head2))

# 1 -> 2 -> 3 -> 4
# -1 -> 0 -> 3 -> 4 -> 5