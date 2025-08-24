import re
import sys

def my_sqrt(n):
    if n < 0:
        return None
    x = n
    for _ in range(10):
        x = 0.5 * (x + n/x)
    return x

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        sqrt_delta = my_sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        print("Discriminant is strictly positive, the two solutions are:")
        print(x1)
        print(x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Discriminant is zero, the solution is:")
        print(x)
    else:
        # Complex solutions
        real = -b / (2*a)
        imag = my_sqrt(-delta) / (2*a)
        print("Discriminant is strictly negative, the two complex solutions are:")
        print(f"{real} + {imag}i")
        print(f"{real} - {imag}i")

def parse_polynomial_side(side):
    coefficients = {}
    
	# Step 1: Define pattern parts
    sign_part = '([+-]?\s*[0-9]*\.?[0-9]+)'      # Matches: +5, -9.3, 4
    middle_part = '\s*\*\s*X\^'                   # Matches: * X^
    power_part = '([0-9]+)'                       # Matches: 0, 1, 2
    
    # Step 2: Combine all parts into full pattern
    pattern = sign_part + middle_part + power_part
    matches = re.findall(pattern, side)
    # print(matches)
    # exit()
    for coeff_str, power_str in matches:
        coeff = float(coeff_str.replace(' ', ''))
        power = int(power_str)
        coefficients[power] = coefficients.get(power, 0) + coeff
        # print(f"power {power}: {coeff}")
        # print(f"coefficients[{power}]: {coefficients[power]}")
    # print(coefficients)
    # exit()
    return coefficients

def parse_equation(equation):
    if '=' not in equation:
        raise ValueError("Invalid equation: missing '=' sign")
    
    # Check for multiple equals signs
    if equation.count('=') > 1:
        raise ValueError("Invalid equation: multiple '=' signs")
    
    left_side, right_side = equation.split('=')
    left_side = left_side.strip()
    right_side = right_side.strip()
    
    # Check for empty sides
    if not left_side and not right_side:
        raise ValueError("Invalid equation: both sides are empty")
    
    # exit()
    left_coeffs = parse_polynomial_side(left_side) if left_side else {}
    right_coeffs = parse_polynomial_side(right_side) if right_side else {}
    # print("left_coeffs =", left_coeffs)
    # exit()
    final_coeffs = left_coeffs.copy()
    for power, coeff in right_coeffs.items():
        # print(power ,coeff)
        final_coeffs[power] = final_coeffs.get(power, 0) - coeff
    # print("Final coefficients:", final_coeffs)
    # exit()
    return final_coeffs

def print_reduced_form(coeffs):
    terms = []
    max_power = max(coeffs.keys())
    # print(max_power)
    # exit()
    for p in range(max_power+1):
        coeff = coeffs.get(p, 0)
        terms.append(f"{coeff} * X^{p}")
    print("Reduced form:", " + ".join(terms), "= 0")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py '<equation>'")
        sys.exit(1)

    equation = sys.argv[1]
    try:
        coeffs = parse_equation(equation)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        print_reduced_form(coeffs)
    except Exception as e:
        print(f"Error while printing reduced form: {e}")
        sys.exit(1)

    # Degree detection
    nonzero = [p for p, c in coeffs.items() if abs(c) > 1e-9]
    if not nonzero:
        print("Any real number is a solution.")
        sys.exit(0)
    degree = max(nonzero)

    print(f"Polynomial degree: {degree}")

    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    elif degree == 2:
        a = coeffs.get(2, 0)
        b = coeffs.get(1, 0)
        c = coeffs.get(0, 0)
        solve_quadratic(a, b, c)
    elif degree == 1:
        b = coeffs.get(1, 0)
        c = coeffs.get(0, 0)
        if b != 0:
            print("The solution is:")
            print(-c / b)
        else:
            print("No solution.")
    else:  # degree == 0
        if coeffs.get(0, 0) == 0:
            print("Any real number is a solution.")
        else:
            print("No solution.")
