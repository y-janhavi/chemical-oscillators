import math  # Importing math module to use tan and cos functions

# Define the function for which we want to find the root
def f(x):
    return 2 * math.sin(x)**2 - math.sin(x) - 1  # Function: tan(x) - x

# Define the derivative of the function
def df(x):
    return 4* math.sin (x)*math.cos (x)-math.cos (x)

# Newton-Raphson Method implementation
def newton_raphson(x0, max_iter, err=0.001):
    # Print table header
    print("Iterations\t\tx\t\tf(x)\t\tf'(x)")

    # Iteratively apply Newton-Raphson formula
    for i in range(max_iter):
        fx = f(x0)   # Evaluate function at current guess
        dfx = df(x0)  # Evaluate derivative at current guess

        # Print current iteration values
        print(f"{i}\t\t{x0}\t\t{fx}\t\t{dfx}")

        if dfx == 0:  # Avoid division by zero
            print("Derivative is zero. No solution found.")
            return None

        # Compute the next approximation using Newton-Raphson formula
        x1 = x0 - fx / dfx

        # Check if the result is within the acceptable error tolerance
        if abs(x1 - x0) < err:
            print(f"Root: {x1}")  # Root found
            return x1

        # Update the guess for the next iteration
        x0 = x1

    # If maximum iterations are reached, return the best approximation
    print(f"Root: {x0}")
    return x0

# Example usage of the Newton-Raphson method
if __name__ == "__main__":
    # Get initial guess and max iteration count from the user
    x0 = float(input("Enter initial guess (x0): "))  # e.g., 4.5
    max_iter = int(input("Enter maximum number of iterations: "))
    
    # Call the Newton-Raphson function
    newton_raphson(x0, max_iter)
