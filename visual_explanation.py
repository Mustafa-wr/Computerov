"""
VISUAL EXPLANATION: How final_coeffs works
==========================================

Example equation: 3*X^2 + 2*X^1 = 1*X^1 + 5*X^0

STEP 1: Parse both sides
========================

LEFT SIDE: 3*X^2 + 2*X^1
┌─────────────────────────────┐
│  Power  │  Coefficient      │
├─────────┼───────────────────┤
│   X^0   │       0           │
│   X^1   │       2           │
│   X^2   │       3           │
└─────────┴───────────────────┘
left_coeffs = {0: 0, 1: 2, 2: 3}

RIGHT SIDE: 1*X^1 + 5*X^0
┌─────────────────────────────┐
│  Power  │  Coefficient      │
├─────────┼───────────────────┤
│   X^0   │       5           │
│   X^1   │       1           │
│   X^2   │       0           │
└─────────┴───────────────────┘
right_coeffs = {0: 5, 1: 1, 2: 0}

STEP 2: Start with left side
============================

final_coeffs = left_coeffs.copy()
┌─────────────────────────────┐
│  Power  │  Coefficient      │
├─────────┼───────────────────┤
│   X^0   │       0           │
│   X^1   │       2           │
│   X^2   │       3           │
└─────────┴───────────────────┘

STEP 3: Subtract right side terms
==================================

Original equation: 3*X^2 + 2*X^1 = 1*X^1 + 5*X^0
Move everything to left: 3*X^2 + 2*X^1 - 1*X^1 - 5*X^0 = 0

For each term in right_coeffs, subtract from final_coeffs:

Iteration 1: power=0, coeff=5
┌─────────────────────────────┐     ┌─────────────────────────────┐
│  Power  │  Before │  After  │     │  Calculation                │
├─────────┼─────────┼─────────┤     ├─────────────────────────────┤
│   X^0   │    0    │   -5    │ <-- │  final_coeffs[0] = 0 - 5   │
│   X^1   │    2    │    2    │     │                             │
│   X^2   │    3    │    3    │     │                             │
└─────────┴─────────┴─────────┘     └─────────────────────────────┘

Iteration 2: power=1, coeff=1
┌─────────────────────────────┐     ┌─────────────────────────────┐
│  Power  │  Before │  After  │     │  Calculation                │
├─────────┼─────────┼─────────┤     ├─────────────────────────────┤
│   X^0   │   -5    │   -5    │     │                             │
│   X^1   │    2    │    1    │ <-- │  final_coeffs[1] = 2 - 1   │
│   X^2   │    3    │    3    │     │                             │
└─────────┴─────────┴─────────┘     └─────────────────────────────┘

Iteration 3: power=2, coeff=0
┌─────────────────────────────┐     ┌─────────────────────────────┐
│  Power  │  Before │  After  │     │  Calculation                │
├─────────┼─────────┼─────────┤     ├─────────────────────────────┤
│   X^0   │   -5    │   -5    │     │                             │
│   X^1   │    1    │    1    │     │                             │
│   X^2   │    3    │    3    │ <-- │  final_coeffs[2] = 3 - 0   │
└─────────┴─────────┴─────────┘     └─────────────────────────────┘

FINAL RESULT
============

final_coeffs = {0: -5, 1: 1, 2: 3}

This represents: -5*X^0 + 1*X^1 + 3*X^2 = 0
Or simplified: 3*X^2 + X^1 - 5 = 0

VISUAL FLOW:
============

    3*X^2 + 2*X^1  =  1*X^1 + 5*X^0
         ↓                    ↓
    [Copy to left]      [Subtract from left]
         ↓                    ↓
    3*X^2 + 2*X^1 - 1*X^1 - 5*X^0 = 0
         ↓
    3*X^2 + 1*X^1 - 5*X^0 = 0

The code does this mathematically by:
- Starting with left side coefficients
- Subtracting each right side coefficient from the corresponding left side coefficient
"""

print("Check the visual explanation above!")
