import math  # Not needed for this program but included for possible future extensions

# Function to perform matrix multiplication of two 3x3 matrices
def matrix_multiply(A, B):
    # Initialize a 3x3 result matrix filled with zeros
    result = [[0 for _ in range(3)] for _ in range(3)]
    
    # Perform the multiplication using three nested loops
    # Outer loop for rows of A
    for i in range(3):
        # Middle loop for columns of B
        for j in range(3):
            # Inner loop to compute the dot product of row i of A and column j of B
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]  # Accumulate the product terms

    return result  # Return the resulting matrix

# Function to take 3x3 matrix input from the user
def get_matrix_input(matrix_name):
    matrix = []
    print(f"Enter the values for {matrix_name} (3x3 matrix):")
    for i in range(3):  # Loop over rows
        # Ask user to enter one row at a time
        row = list(map(float, input(f"Enter row {i + 1} (space-separated values): ").split()))
        
        # Ensure the user enters exactly 3 numbers
        while len(row) != 3:
            print("Please enter exactly 3 values.")
            row = list(map(float, input(f"Enter row {i + 1} (space-separated values): ").split()))
        
        matrix.append(row)  # Add the row to the matrix
    return matrix  # Return the completed matrix

# Main program
if __name__ == "__main__":
    # Get user input for the two matrices
    A = get_matrix_input("Matrix A")
    B = get_matrix_input("Matrix B")
    
    # Multiply the two matrices
    result = matrix_multiply(A, B)
    
    # Display the result
    print("Result of matrix multiplication:")
    for row in result:
         print(row)  # Print each row of the result matrix
