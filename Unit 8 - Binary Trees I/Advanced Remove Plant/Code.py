from collections import deque

class TreeNode():
     def __init__(self, value, left=None, right=None):
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

def remove_plant(collection, name):
    if not collection:
        return collection
    
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        # No children
        if collection.left is None and collection.right is None:
            return None
        
        # One child
        if collection.left is None:
            return collection.right
        if collection.right is None:
            return collection.left
        
        # Two children
        predecessor = max_left(collection.left)
        collection.val = predecessor.val
        collection.left = remove_plant(collection.left, predecessor.val)

    return collection


def max_left(collection):
    if not collection.right:
        return collection
    current = collection.right
    while current.right != None:
        current = current.right
    return current

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))

# ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

# Explanation:
# The resulting tree structure:
#              Money Tree
#             /         \
#           Hoya       Orchid
#               \          \
#               Ivy      ZZ Plant