from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def larger_order_tree(order_tree, order):
    # bfs
    if not order_tree:
        return
    
    deq = deque([order_tree])
    res = []

    while deq:
        lev = len(deq)
        lev_nodes = []

        for i in range(lev):
            curr_node = deq.popleft()

            if curr_node == order:
                if i == lev - 1:
                    return TreeNode(None)
                else:
                    return deq.popleft()

            if curr_node.left:
                deq.append(curr_node.left)
            if curr_node.right:
                deq.append(curr_node.right)

    res.append(lev_nodes)

    return res


# """
#         Cupcakes
#        /       \ 
#    Macaron     Cookies      
#         \      /      \
#       Cake   Eclair   Croissant
# """
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)
# Eclair
# None