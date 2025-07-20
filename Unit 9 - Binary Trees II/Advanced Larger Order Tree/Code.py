from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def larger_order_tree(orders):
    def reverse_inorder(node, cumulative_sum):
        if not node:
            return cumulative_sum
        
        cumulative_sum = reverse_inorder(node.right, cumulative_sum)
        node.val += cumulative_sum
        cumulative_sum = node.val
        
        return reverse_inorder(node.left, cumulative_sum)
    
    reverse_inorder(orders, 0)
    return orders


# """
#          4
#        /   \
#       /     \
#      1       6
#     / \     / \
#    0   2   5   7
#         \       \
#          3       8   
# """
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))

# [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
# Explanation:
# Larger Order Tree:
#         30
#        /   \
#       /     \
#      36     21
#     / \     / \
#    36  35  26  15
#          \       \
#          33       8