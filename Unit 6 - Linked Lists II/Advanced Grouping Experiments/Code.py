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

def odd_even_experiments(exp_results):
    if exp_results is None:
        return exp_results
    
    odd = exp_results
    curr = exp_results.next

    while curr and curr.next:
        temp = curr.next
        curr.next = curr.next.next
        curr = curr.next

        temp.next = odd.next
        odd.next = temp
        odd = temp
    
    return exp_results

experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_list(odd_even_experiments(experiment_results1))
print_linked_list(odd_even_experiments(experiment_results2))

# 1 -> 3 -> 5 -> 2 -> 4
# 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4