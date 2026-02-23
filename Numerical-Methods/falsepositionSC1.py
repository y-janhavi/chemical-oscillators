import math

def f(x):
    # Define the function for which we want to find the root
    return x**2 - 25  # This represents the equation x^2 - 25 = 0

def false_position(a, b, max_iter, err=0.001):
    # Check if the function has different signs at the endpoints a and b
    if f(a) * f(b) >= 0:
        print("The function must have different signs at a and b.")
        return None

    # Print the header for the output table
    print("Iterations\t\ta\t\tb\t\tc\t\tf(a)\t\tf(b)\t\tf(c)")
    
    for i in range(max_iter):
        # Calculate the point c using the False Position formula
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        
        # Print the current iteration details
        print(f"{i}\t\t{a}\t\t{b}\t\t{c}\t\t{f(a)}\t\t{f(b)}\t\t{f(c)}")
        
        # Check if c is the root or if the function value at c is small enough
        if f(c) == 0 or abs(f(c)) < err:
            print(f"Root: {c}")
            return c
        
        # Update the interval based on the sign of f(c)
        if f(a) * f(c) < 0:  # Root is in the left subinterval
            b = c  # Update b to c
        else:  # Root is in the right subinterval
            a = c  # Update a to c
            
    # If the maximum number of iterations is reached, return the last computed root
    root = c
    print(f"Root: {root}")
    return root

# Example usage
if __name__ == "__main__":
    # Prompt the user for input values
    a = float(input("Enter lower guess (a): "))  # e.g., 0
    b = float(input("Enter upper guess (b): "))  # e.g., 6
    max_iter = int(input("Enter maximum number of iterations: "))  # e.g., 100
    
    # Call the false_position function with the user inputs
    false_position(a, b, max_iter)