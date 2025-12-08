import numpy as np
import time

np.random.seed(1350)  # Use course number as seed

def problem1():
    """
    Complete the following tasks:
    """
    arr1 = np.arange(10, 51, 5)
    
    arr2 = np.zeros((3, 4))
    
    identity = np.eye(3)
    
    linspace_arr = np.linspace(0, 5, 10)
    
    random_arr = np.random.rand(2, 5)
    
    return arr1, arr2, identity, linspace_arr, random_arr

def problem2():
    """ 
    Perform array operations using broadcasting.
    """ 
    # Given arrays
    arr_a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    
    result_add = arr_a + arr_b
    
    result_multiply = arr_a * arr_b
    
    result_square = arr_a ** 2
    
    column_means = np.mean(arr_a, axis=0)
    
    centered_arr = arr_a - column_means
    
    return result_add, result_multiply, result_square, column_means, centered_arr

def problem3():
    """  
    Demonstrate array indexing and slicing.
    """  
    # Create a 5x5 array with values from 1 to 25
    arr = np.arange(1, 26).reshape(5, 5)
    
    third_row = arr[2, :]
    
    last_column = arr[:, -1]
    
    center_subarray = arr[1:3, 1:3]
    
    greater_than_15 = arr[arr > 15]
    
    arr_copy = arr.copy()
    arr_copy[arr_copy % 2 == 0] = -1
    
    return third_row, last_column, center_subarray, greater_than_15, arr_copy

def problem4():
    """
    Perform statistical analysis on student scores.
    """
    scores = np.array([[85, 90, 78, 92],
                       [79, 85, 88, 91],
                       [92, 88, 95, 89],
                       [75, 72, 80, 78],
                       [88, 91, 87, 94]])
    
    student_averages = np.mean(scores, axis=1)
    
    test_averages = np.mean(scores, axis=0)
    
    student_max_scores = np.max(scores, axis=1)
    
    test_std = np.std(scores, axis=0)
    
    high_performers = student_averages > 85
    
    return student_averages, test_averages, student_max_scores, test_std, high_performers

def problem5():
    """
    Compare performance between NumPy arrays and Python lists.
    Complete the timing comparisons.
    """
    size = 100000
    
    # Create Python list and NumPy array with same data
    python_list = list(range(size))
    numpy_array = np.arange(size)
    
    
    # Python list approach
    start_time = time.time()
    list_result = [x ** 2 for x in python_list]
    list_time = time.time() - start_time
    
    # NumPy array approach
    start_time = time.time()
    array_result = numpy_array ** 2
    numpy_time = time.time() - start_time
    
    # Calculate speedup
    speedup = list_time / numpy_time
    
    # Return times and speedup factor
    return {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
    }

def problem6():
    """
    Note: There seems to be a numbering issue in the PDF. 
    This function appears to be the same as problem5.
    """
    return problem5()

def bonus_challenge():
    """
    Create a simple 10x10 'image' and apply transformations.
    """
    # Create a 10x10 array representing a grayscale image
    # Values should be between 0 (black) and 255 (white)
    image = np.random.randint(0, 256, size=(10, 10))
    
    # a) Normalize the image (scale values to 0-1 range)
    normalized = image / 255.0
    
    # b) Apply brightness adjustment (increase all values by 50, cap at 255)
    brightened = np.clip(image + 50, 0, 255)
    
    # c) Create a negative of the image (invert values)
    negative = 255 - image
    
    # d) Apply threshold (values > 128 become 255, others become 0)
    thresholded = np.where(image > 128, 255, 0)
    
    return normalized, brightened, negative, thresholded

# Testing code
if __name__ == "__main__":
    print("Problem 1 Results:")
    p1_results = problem1()
    print(f"arr1: {p1_results[0]}")
    print(f"arr2 shape: {p1_results[1].shape}")
    print(f"identity shape: {p1_results[2].shape}")
    print(f"linspace_arr: {p1_results[3]}")
    print(f"random_arr shape: {p1_results[4].shape}")
    
    print("\nProblem 2 Results:")
    p2_results = problem2()
    print(f"result_add:\n{p2_results[0]}")
    print(f"result_multiply:\n{p2_results[1]}")
    print(f"result_square:\n{p2_results[2]}")
    print(f"column_means: {p2_results[3]}")
    print(f"centered_arr:\n{p2_results[4]}")
    
    print("\nProblem 3 Results:")
    p3_results = problem3()
    print(f"third_row: {p3_results[0]}")
    print(f"last_column: {p3_results[1]}")
    print(f"center_subarray:\n{p3_results[2]}")
    print(f"greater_than_15: {p3_results[3]}")
    print(f"arr_copy:\n{p3_results[4]}")
    
    print("\nProblem 4 Results:")
    p4_results = problem4()
    print(f"student_averages: {p4_results[0]}")
    print(f"test_averages: {p4_results[1]}")
    print(f"student_max_scores: {p4_results[2]}")
    print(f"test_std: {p4_results[3]}")
    print(f"high_performers: {p4_results[4]}")
    
    print("\nProblem 5 Results:")
    p5_results = problem5()
    print(f"List time: {p5_results['list_time']:.6f} seconds")
    print(f"NumPy time: {p5_results['numpy_time']:.6f} seconds")
    print(p5_results['conclusion'])
    
    print("\nProblem 6 Results:")
    p6_results = problem6()
    print(f"List time: {p6_results['list_time']:.6f} seconds")
    print(f"NumPy time: {p6_results['numpy_time']:.6f} seconds")
    print(p6_results['conclusion'])
    
    print("\nBonus Challenge Results:")
    bonus_results = bonus_challenge()
    print(f"Normalized range: [{bonus_results[0].min():.2f}, {bonus_results[0].max():.2f}]")
    print(f"Brightened range: [{bonus_results[1].min()}, {bonus_results[1].max()}]")
    print(f"Negative range: [{bonus_results[2].min()}, {bonus_results[2].max()}]")
    print(f"Thresholded unique values: {np.unique(bonus_results[3])}")