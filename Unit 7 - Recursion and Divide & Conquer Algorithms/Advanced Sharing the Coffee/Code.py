def can_split_coffee(coffee, n):
    total = 0
    
    def recursive_sum(coffee):
        if not coffee:
            return 0
        return coffee[0] + recursive_sum(coffee[1:])

    return True if recursive_sum(coffee) % n == 0 else False

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

# True
# False