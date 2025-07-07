def next_greatest_letter(letters, target):
    def binary_search(left, right):
        if left > right:
            return letters[left] if left < len(letters) else letters[0]

        mid = (left + right) // 2

        if letters[mid] <= target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    return binary_search(0, len(letters) - 1)


letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))

# b
# Example 1 Explanation: The smallest character lexicographically greater than 'a' in letters is 'b'

# e
# Example 2 Explanation: The smallest character lexicographically greater than 'd' in letters is 'e'

# a
# Example 3 Explanation: There is no character lexicographically greater than 'y' in letters
# so we return letters[0]