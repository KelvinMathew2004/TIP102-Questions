def find_frequency_positions(transmissions, target_code):
    def find_first(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if transmissions[mid] == target_code:
            if mid == 0 or transmissions[mid - 1] < target_code:
                return mid
            return find_first(left, mid - 1)
        elif transmissions[mid] < target_code:
            return find_first(mid + 1, right)
        else:
            return find_first(left, mid - 1)

    def find_last(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if transmissions[mid] == target_code:
            if mid == len(transmissions) - 1 or transmissions[mid + 1] > target_code:
                return mid
            return find_last(mid + 1, right)
        elif transmissions[mid] < target_code:
            return find_last(mid + 1, right)
        else:
            return find_last(left, mid - 1)

    first = find_first(0, len(transmissions) - 1)
    last = find_last(0, len(transmissions) - 1)
    return (first, last)