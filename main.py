import cmath
import re

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    print("Discriminant:", delta)

    sqrt_delta = cmath.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2*a)
    x2 = (-b - sqrt_delta) / (2*a)

    if delta > 0:
        print("Two real solutions:")
        print(f"x1 = {x1.real}")
        print(f"x2 = {x2.real}")
    elif delta == 0:
        print("One real solution:")
        print(f"x = {x1.real}")
    else:
        print("Two complex solutions:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

def parse_polynomial_side(side):
    """Parse one side of equation like '5 * X^0 + 4 * X^1 - 9.3 * X^2'"""
    coefficients = {}
    
    pattern = r'([+-]?\s*[0-9]*\.?[0-9]+)\s*\*\s*X\^([0-9]+)'
    matches = re.findall(pattern, side)
    # print (f"Matches found: {matches}")
    
    for coeff_str, power_str in matches:
        coeff = float(coeff_str.replace(' ', ''))  # Remove spaces and convert
        power = int(power_str)
        
        if power in coefficients:
            coefficients[power] += coeff  # Add if same power exists
        else:
            coefficients[power] = coeff
    
    return coefficients

def parse_equation(equation):
    """Parse full equation like '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'"""
    # Split by equals sign
    if '=' not in equation:
        raise ValueError("Invalid equation: missing '=' sign")
    
    left_side, right_side = equation.split('=')

    left_coeffs = parse_polynomial_side(left_side.strip())
    right_coeffs = parse_polynomial_side(right_side.strip())
    
    # Move right side to left: left - right = 0
    # So we subtract right side coefficients from left side
    final_coeffs = left_coeffs.copy()
    
    for power, coeff in right_coeffs.items():
        if power in final_coeffs:
            final_coeffs[power] -= coeff
        else:
            final_coeffs[power] = -coeff
    
    return final_coeffs

# Test the parser
print("Testing individual sides:")
side1 = "5 * X^0 + 4 * X^1 - 9.3 * X^2"
result = parse_polynomial_side(side1)
print(f"Input: {side1}")
print(f"Parsed: {result}")

side2 = "1 * X^0"
result2 = parse_polynomial_side(side2)
print(f"Input: {side2}")
print(f"Parsed: {result2}")

print("\nTesting full equation:")
equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
result3 = parse_equation(equation)
print(f"Input: {equation}")
print(f"Reduced: {result3}")