# ==============================
# PROBLEM 1: Grade Book Dictionary
# ==============================

def add_student(gradebook, name, grade):
    if 0 <= grade <= 100:
        gradebook[name] = grade
        return True
    return False

def get_class_average(gradebook):
    if not gradebook:
        return 0
    return sum(gradebook.values()) / len(gradebook)

# Bonus -- 10 points
def get_passing_students(gradebook):
    return [name for name, grade in gradebook.items() if grade >= 60]

# ==============================
# PROBLEM 2: Regular Expressions
# ==============================

import re

def find_all_phones(text):
    # Matches xxx-xxx-xxxx or (xxx) xxx-xxxx
    pattern = r'\b\d{3}-\d{3}-\d{4}\b|\(\d{3}\) \d{3}-\d{4}'
    return re.findall(pattern, text)

def find_all_prices(text):
    # Matches $x.xx, $xx.xx, $xxx.xx, etc.
    pattern = r'\$\d+\.\d{2}'
    return re.findall(pattern, text)

def extract_emails(text):
    # Simple email pattern: word@word.word
    pattern = r'\b\w+@\w+\.\w+\b'
    return re.findall(pattern, text)

def validate_student_id(student_id):
    # Exactly 2 letters followed by 4 digits
    pattern = r'^[A-Za-z]{2}\d{4}$'
    return bool(re.match(pattern, student_id))

# ==============================
# TESTING ALL FUNCTIONS
# ==============================

if __name__ == "__main__":
    print("=== PROBLEM 1: Grade Book Tests ===")
    gradebook = {}

    print(add_student(gradebook, "Alice", 85))    # Should print True
    print(add_student(gradebook, "Bob", 150))     # Should print False
    print(add_student(gradebook, "Charlie", 45))  # Should print True

    print(f"Average: {get_class_average(gradebook):.2f}")
    print(f"Passing: {get_passing_students(gradebook)}")
    
    print("\n=== PROBLEM 2: Regex Tests ===")
    test_text = """For info, call 555-123-4567 or (555) 987-6543.
Email us at info@school.com or admin@college.com
Course fees: $50.00 for materials, $150.50 for tuition"""

    print("phones:", find_all_phones(test_text))
    print("prices:", find_all_prices(test_text))
    print("emails:", extract_emails(test_text))

    print("Valid ID 'AB1234':", validate_student_id("AB1234"))   # True
    print("Valid ID 'G51234':", validate_student_id("G51234"))   # False
    print("Valid ID '120802':", validate_student_id("120802"))   # False
    print("Valid ID 'AB12345':", validate_student_id("AB12345")) # False