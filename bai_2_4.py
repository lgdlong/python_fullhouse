import math

a, b, r = map(float, input().split())

remaining_area_rounded = round(a * b - math.pi * r**2, 2)

# Print the result
print(remaining_area_rounded)
