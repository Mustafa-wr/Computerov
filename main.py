import cmath

def solve_quadratic(a, b, c):
    
    delta = b**2 - 4*a*c
    print("Discriminant:", delta)

   
    sqrt_delta = cmath.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)

   
    if delta > 0:
        print("Two real solutions:")
        print(x1, x2)
    elif delta == 0:
        print("One real solution:")
        print(x1)  # x1 and x2 are equal
    else:
        print("Two complex solutions:")
        print(x1, x2)

print("Test 1: X^2 + 2X + 1 = 0")
solve_quadratic(1, 2, 1)

print("\nTest 2: X^2 + 0X - 1 = 0")
solve_quadratic(1, 0, -1)

print("\nTest 3: X^2 + 2X + 5 = 0")
solve_quadratic(1, 2, 5)