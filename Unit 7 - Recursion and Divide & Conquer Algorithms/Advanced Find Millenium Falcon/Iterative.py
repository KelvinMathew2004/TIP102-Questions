def check_stock(inventory, part_id):
    inventory.sort()
    left, right = 0, len(inventory)-1

    while left <= right:
        mid = (left+right) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            left = mid+1
        else:
            right = mid - 1
    
    return False

    
print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))

# True
# False