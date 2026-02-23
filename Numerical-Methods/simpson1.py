import math

# Simpson's 1/3 Rule with table
def simpsons_one_third(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's 1/3 Rule")
        
    h = (b - a) / n
    result = f(a) + f(b)

    print(f"\nStep size (h) = {h:.4f}\n")
    print(f"{'i':<3} {'x':<10} {'f(x)':<10} {'Weight':<7} {'Running Sum'}")
    print("-" * 45)
    
    print(f"{0:<3} {a:<10.4f} {f(a):<10.4f} {1:<7} {result:<10.4f}")
    
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        weight = 4 if i % 2 == 1 else 2
        result += weight * fx
        print(f"{i:<3} {x:<10.4f} {fx:<10.4f} {weight:<7} {result:<10.4f}")
    
    print(f"{n:<3} {b:<10.4f} {f(b):<10.4f} {1:<7} {'-'}")

    integral = result * (h / 3)
    print("\n" + "=" * 45)
    return integral

# Example: Integrate x**3 from 0 to 1
def func(x):
    return x**3

a1 = 0
b1 = 1
n1 = 10  # Must be even

integral = simpsons_one_third(func,a1,b1,n1)
print(f"Integral of x**3 from {a1} to {b1} ≈ {integral}")
