import math

a, b, r = map(float, input().split())

res = a * b - math.pi*(r**2)

new_res = round(res, 2)

print(new_res)