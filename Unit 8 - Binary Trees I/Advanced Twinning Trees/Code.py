class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root1 and root2:
        return False
    elif root1 and not root2:
        return False
    elif not root1 and not root2:
        return True

    if root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right):
        return True
    else:
        return False

# """
#       1                1
#      / \              / \
#     2   3            2   3  
# """

root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

# """
#       1                1
#      /                  \
#     2                    2  
# """

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))

# True
# False