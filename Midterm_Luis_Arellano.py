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

# Test your functions
if __name__ == "__main__":
    gradebook = {}

    print(add_student(gradebook, "Alice", 85))    # Should print True
    print(add_student(gradebook, "Bob", 150))     # Should print False
    print(add_student(gradebook, "Charlie", 45))  # Should print True

    print(f"Average: {get_class_average(gradebook):.2f}")
    # Bonus -- 10 points
    print(f"Passing: {get_passing_students(gradebook)}")