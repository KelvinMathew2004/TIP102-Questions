def find_closest_planets(planets, target_distance, k):
    def binary_search(left, right):
        if left > right:
            return left if left < len(planets) else right

        mid = (left + right) // 2

        if planets[mid] <= target_distance:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    closest = binary_search(0, len(planets) - 1)

    start = max(closest - (k-1), 0)
    end = min(closest + (k-1), len(planets)-1)

    left = start
    right = closest

    minRange, leastClosest, mostClosest = float('inf'), 0, 0

    while right <= end:
        if abs(planets[right]-planets[left]) < minRange:
            minRange = abs(planets[right]-planets[left])
            leastClosest = left
            mostClosest = right
        left += 1
        right += 1

    return planets[leastClosest:mostClosest+1]


planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]

print(find_closest_planets(planets1, 350, 3))
print(find_closest_planets(planets2, 25, 2))

# [200, 300, 400]
# [20, 30]