import math  # Importing math module (not needed in current version, but useful for more complex functions)

# Define the function for which we are finding the root
def f(x):
    return 3*x**2 + 4*x - 15  # Root(s) of this function occur where x^2 = 25, i.e., x = ±5

# Function to perform the Bisection Method
def bisection(a, b, max_iter, err=0.001):
    # Display header for iteration table
    print("Iterations\t\tx0\t\tx1\t\tx2\t\tf(x0)\t\tf(x1)\t\tf(x2)")
    
    # Loop up to the specified number of iterations
    for i in range(max_iter):
        c = (a + b) / 2  # Calculate midpoint of the interval [a, b]
        
        # Print the current values for this iteration
        print(f"{i}\t\t{a}\t\t{b}\t\t{c}\t\t{f(a)}\t\t{f(b)}\t\t{f(c)}")
        
        # Check if f(c) is 0, meaning we've found the exact root
        if f(c) == 0:
            print(f"Root: {c}")
            return c  # Exit and return the root
        
        # Determine which subinterval contains the root based on sign of f(c)
        elif f(a) * f(c) < 0:
            b = c  # Root lies in the left subinterval [a, c]
        else:
            a = c  # Root lies in the right subinterval [c, b]
    
    # After all iterations, return the midpoint as the approximate root
    root = (a + b) / 2
    print(f"Root: {root}")
    return root

# Entry point of the script
if __name__ == "__main__":
    # Get user input for initial guesses and maximum iterations
    a = float(input("Enter guess 1: "))  # First guess (start of interval)
    b = float(input("Enter guess 2: "))  # Second guess (end of interval)
    max_iter = int(input("Enter maximum number of iterations: "))  # How many times to repeat
    
    # Call the bisection function with the provided input
    bisection(a, b, max_iter)
