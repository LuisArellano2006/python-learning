def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    """
    try:
        # Convert inputs to float first
        num_a = float(a)
        num_b = float(b)
        # Check for division by zero
        if num_b == 0:
            return "Error: Cannot divide by zero"
        return num_a / num_b
    except (ValueError, TypeError):
        return "Error: Invalid input"

# Test cases
print(safe_divide(10, 2))       # 5.0
print(safe_divide("10", "2"))   # 5.0
print(safe_divide(10, 0))       # Error: Cannot divide by zero
print(safe_divide("abc", 2))    # Error: Invalid input

def sum_of_digits(n):
    """
    Calculate the sum of all digits in a number using recursion.
    """
    # Base case: single digit or zero
    if n == 0:
        return 0
    # Recursive case
    last_digit = n % 10
    remaining = n // 10
    return last_digit + sum_of_digits(remaining)

# Test cases
print(sum_of_digits(123))    # 6
print(sum_of_digits(4567))   # 22
print(sum_of_digits(5))      # 5
print(sum_of_digits(0))      # 0