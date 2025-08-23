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
    
    print(f"Input: '{side}'")
    print(f"Matches found: {matches}")
    
    for coeff_str, power_str in matches:
        coeff = float(coeff_str.replace(' ', ''))
        power = int(power_str)
        coefficients[power] = coefficients.get(power, 0) + coeff
    
    print(f"Parsed coefficients: {coefficients}")
    return coefficients

# Test the problematic case
print("Testing the problematic input...")
print("=" * 50)

left_side = "5 * X^0 + 4 * X^1 - 9.3 ** X^2"
right_side = "9x"

print("LEFT SIDE:")
left_coeffs = parse_polynomial_side(left_side)

print("\nRIGHT SIDE:")
right_coeffs = parse_polynomial_side(right_side)

print("\nFINAL RESULT:")
final_coeffs = left_coeffs.copy()
for power, coeff in right_coeffs.items():
    final_coeffs[power] = final_coeffs.get(power, 0) - coeff

print(f"Final coefficients: {final_coeffs}")

# Show what terms were silently ignored
print("\nANALYSIS:")
print("Terms that were successfully parsed:")
print(f"- Left side: 5 * X^0, 4 * X^1")
print("Terms that were IGNORED:")
print(f"- Left side: '- 9.3 ** X^2' (invalid ** operator)")
print(f"- Right side: '9x' (not in polynomial format)")
print("\nThis could be misleading to the user!")
