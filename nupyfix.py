import os
import sys
import subprocess

def fix_numpy_installation():
    """Fix NumPy installation for Python 3.13"""
    
    # Change to a safe directory
    os.chdir(os.path.expanduser('~'))
    print("Working from:", os.getcwd())
    
    # Try to uninstall and reinstall NumPy
    try:
        print("Uninstalling current NumPy...")
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "numpy", "-y"])
        
        print("Installing NumPy compatible with Python 3.13...")
        # Try installing from a specific wheel or pre-release
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--pre", "numpy", "--force-reinstall"])
        
        # Test the installation
        import numpy as np
        print(f"Success! NumPy version: {np.__version__}")
        
        # Run your practice code
        practice_1_review(np)
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTrying alternative installation method...")
        
        # Try installing from a specific URL
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", 
                                  "https://github.com/numpy/numpy/releases/download/v2.0.0rc1/numpy-2.0.0rc1-cp313-cp313-win_amd64.whl"])
            
            import numpy as np
            print(f"Success! NumPy version: {np.__version__}")
            practice_1_review(np)
            
        except Exception as e2:
            print(f"Failed with alternative method: {e2}")
            print("\nPlease try using Python 3.12 instead of 3.13.")
            print("You can download Python 3.12 from: https://www.python.org/downloads/")

def practice_1_review(np):
    """
    Quick Review Exercise: Array Operations
    """
    print("\n" + "="*50)
    print("REVIEW EXERCISE: Array Basics")
    print("="*50)
    
    # Given array of temperatures
    temps = np.array([68, 72, 75, 71, 77, 73, 70])    
    print("This week's temperatures:", temps)
    
    # Add 5 degrees to all temperatures
    heat_wave = temps + 5

    # Convert to Celsius
    celsius = (temps - 32) * 5/9

    # Find temperatures above 72
    warm_days = temps > 72

    print(f"Heat wave temps: {heat_wave}")
    print(f"In Celsius: {celsius}")
    print(f"Days above 72°F: {warm_days}")
    print(f"Number of warm days: {np.sum(warm_days)}")

if __name__ == "__main__":
    fix_numpy_installation()