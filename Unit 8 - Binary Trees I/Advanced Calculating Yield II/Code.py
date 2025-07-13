class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  if root is None:
     return
  
  if root.left is None and root.right is None:
     return root.val
  
  l = calculate_yield(root.left)
  r = calculate_yield(root.right)
  
  if root.val == "+":
     return l + r
  elif root.val == "-":
     return l - r
  elif root.val == "*":
     return l * r
  else:
     return l / r     


# """
#       +
#      / \ 
#     /   \
#    -     *
#   / \   / \
#  4   2 10  2
# """

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

# 22
# Explanation:
# - 4 - 2 = 2
# - 10 * 2 = 20
# - 2 + 20 = 22