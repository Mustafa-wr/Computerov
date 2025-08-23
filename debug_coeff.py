import re

def parse_polynomial_side(side):
    coefficients = {}
    
    # Step 1: Define pattern parts
    sign_part = '([+-]?\s*[0-9]*\.?[0-9]+)'      # Matches: +5, -9.3, 4
    middle_part = '\s*\*\s*X\^'                   # Matches: * X^
    power_part = '([0-9]+)'                       # Matches: 0, 1, 2
    
    # Step 2: Combine all parts into full pattern
    pattern = sign_part + middle_part + power_part
    matches = re.findall(pattern, side)
    print(f"Parsing '{side}':")
    print(f"Regex matches: {matches}")
    
    for coeff_str, power_str in matches:
        coeff = float(coeff_str.replace(' ', ''))
        power = int(power_str)
        print(f"  Found: {coeff_str} -> coeff={coeff}, power={power}")
        coefficients[power] = coefficients.get(power, 0) + coeff
    
    print(f"Final coefficients: {coefficients}")
    return coefficients

# Test the right side parsing
print("=== TESTING RIGHT SIDE PARSING ===")
right_side = "1*X^1 + 5*X^0"
right_coeffs = parse_polynomial_side(right_side)

print(f"\nright_coeffs = {right_coeffs}")
print(f"\nIterating through right_coeffs.items():")
for i, (power, coeff) in enumerate(right_coeffs.items()):
    print(f"Iteration {i+1}: power={power}, coeff={coeff}")
