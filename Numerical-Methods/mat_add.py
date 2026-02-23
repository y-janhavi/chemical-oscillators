# Initialize matrices and dimensions
a = []
b = []
c = []

# Take input for rows and columns
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

# Input elements for the first matrix
print("Enter elements of first matrix:")
for i in range(row):
    temp = []
    for j in range(col):
        value = int(input(f"a{i+1}{j+1}: "))
        temp.append(value)
    a.append(temp)

# Display first matrix
print("First Matrix:")
for i in range(row):
    for j in range(col):
        print(f"{a[i][j]} ", end='')
    print()

# Input elements for the second matrix
print("Enter elements of second matrix:")
for i in range(row):
    temp = []
    for j in range(col):
        value = int(input(f"b{i+1}{j+1}: "))
        temp.append(value)
    b.append(temp)

# Display second matrix
print("Second Matrix:")
for i in range(row):
    for j in range(col):
        print(f"{b[i][j]} ", end='')
    print()

# Add the two matrices
print("Resultant Matrix (c = a + b):")
for i in range(row):
    row_result = []
    for j in range(col):
        row_result.append(a[i][j] + b[i][j])
    c.append(row_result)

# Display the resultant matrix
for i in range(row):
    for j in range(col):
        print(f"{c[i][j]} ", end='')
    print()
