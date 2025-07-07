def check_stock(inventory, part_id):
    def binary_search(left, right):
        if left > right:
            return False
        
        mid = (left + right) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    return binary_search(0, len(inventory) - 1)


print(check_stock([1, 2, 5, 20], 20))
print(check_stock([1, 2, 5, 20], 100))

# True
# False