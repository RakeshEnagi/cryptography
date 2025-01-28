def extended_gcd(a, b):
    steps = []
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        r = a % b

        steps.append([a, b, r, q, x1, y1])

        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    steps.append([a, b, a, None, x0, y0])
    
    return steps, a, x0, y0

def print_steps(steps):
    print(f"{'Step':<6}{'a':<6}{'b':<6}{'a % b':<10}{'Quotient':<10}{'x':<6}{'y':<6}")
    for i, step in enumerate(steps):
        quotient = step[3] if step[3] is not None else "N/A"
        print(f"{i+1:<6}{step[0]:<6}{step[1]:<6}{step[2]:<10}{quotient:<10}{step[4]:<6}{step[5]:<6}")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
steps, gcd, x, y = extended_gcd(a, b)

print_steps(steps)

print(f"\nGCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
