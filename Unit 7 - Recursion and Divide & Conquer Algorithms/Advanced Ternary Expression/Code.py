def evaluate_ternary_expression_recursive(expression):
    if len(expression) == 1:
        return expression

    condition = expression[0]
    i = 2
    count = 0

    while i < len(expression):
        if expression[i] == '?':
            count += 1
        elif expression[i] == ':':
            if count == 0:
                break
            count -= 1
        i += 1

    true_expr = expression[2:i]
    false_expr = expression[i + 1:]

    if condition == 'T':
        return evaluate_ternary_expression_recursive(true_expr)
    else:
        return evaluate_ternary_expression_recursive(false_expr)

print(evaluate_ternary_expression_recursive("T?2:3"))  # Output: 2
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))  # Output: 4
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))  # Output: F