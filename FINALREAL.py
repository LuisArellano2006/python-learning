# ----------------------------------------------------
# Problem 1: File Line Counter
# ----------------------------------------------------

def count_lines_with_word(filename, word):
    count = 0
    word = word.lower()

    try:
        with open(filename, "r") as file:
            for line in file:
                if word in line.lower():
                    count += 1
    except FileNotFoundError:
        return 0

    return count


# TEST CODE (ACTIVE)
print("Problem 1 Output:")
print(count_lines_with_word("file.txt", "hello"))
print("----------------------------------------")


# ----------------------------------------------------
# Problem 2: Bank Account Class
# ----------------------------------------------------

class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance

    def get_balance(self):
        return self.balance


# TEST CODE (ACTIVE)
print("Problem 2 Output:")
account = BankAccount("John", 100)
print(account.deposit(50))     # 150
print(account.withdraw(30))    # 120
print(account.withdraw(200))   # insufficient funds + 120
print("----------------------------------------")


# ----------------------------------------------------
# Problem 3: Safe Calculator
# ----------------------------------------------------

def safe_calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Invalid operation"

    except ValueError:
        return "Error: Invalid number"

    except ZeroDivisionError:
        return "Error: Division by zero"


# TEST CODE (ACTIVE)
print("Problem 3 Output:")
print(safe_calculate(10, 5, '+'))
print(safe_calculate("10", "5", '-'))
print(safe_calculate(10, 0, '/'))
print(safe_calculate("abc", 5, '+'))
print("----------------------------------------")


# ----------------------------------------------------
# Problem 4: Recursive Palindrome Checker
# ----------------------------------------------------

def is_palindrome_recursive(s):
    s = ''.join(c.lower() for c in s if c.isalnum())

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome_recursive(s[1:-1])


# TEST CODE (ACTIVE)
print("Problem 4 Output:")
print(is_palindrome_recursive("racecar"))
print(is_palindrome_recursive("hello"))
print(is_palindrome_recursive("A man a plan a canal Panama"))
print(is_palindrome_recursive(""))
print("----------------------------------------")


# ----------------------------------------------------
# Problem 5: Student Grade Analysis
# ----------------------------------------------------

def analyze_grades(students):
    student_averages = list(
        map(lambda student: (student[0], sum(student[1]) / len(student[1])), students)
    )

    passing = list(filter(lambda s: s[1] >= 70, student_averages))
    failing = list(filter(lambda s: s[1] < 70, student_averages))

    highest = max(student_averages, key=lambda s: s[1])[0]

    class_avg = sum(s[1] for s in student_averages) / len(student_averages)

    return {
        "passing": [s[0] for s in passing],
        "failing": [s[0] for s in failing],
        "highest": highest,
        "class_average": round(class_avg, 1)
    }


# TEST CODE (ACTIVE)
print("Problem 5 Output:")
test_data = [
    ('Alice', [85, 90, 88]),
    ('Bob', [60, 65, 62]),
    ('Charlie', [75, 80, 77]),
    ('Diana', [95, 92, 94])
]

print(analyze_grades(test_data))
print("----------------------------------------")
