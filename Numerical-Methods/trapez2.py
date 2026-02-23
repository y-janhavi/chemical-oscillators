def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    print(f"{'i':<5} {'x':<15} {'f(x)':<15} {'Running Sum':<15}")
    print("-" * 50)
    print(f"{0:<5} {a:<15.8f} {f(a):<15.8f} {result:<15.8f}")

    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        result += fx
        print(f"{i:<5} {x:<15.8f} {fx:<15.8f} {result:<15.8f}")

    print(f"{n:<5} {b:<15.8f} {f(b):<15.8f} {'-':<15}")
    return result * h

# Function 1
def func1(x):
    return 1/(1+x**2)

# Parameters
a = 0
b = 1

n = 10  

integral = trapezoidal_rule(func1, a, b, n)
print(f"\nIntegral of1/( 1 + x^2) from {a} to {b} ≈{integral}")