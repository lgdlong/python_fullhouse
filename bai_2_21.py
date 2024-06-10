import math

x, y, u, v = map(int, input().split())

length = math.sqrt(x**2 + y**2) - math.sqrt(u**2 + v**2)

if (length == 0):
    print('BANG NHAU')
elif (length < 0):
    print('A')
else:
    print('B')