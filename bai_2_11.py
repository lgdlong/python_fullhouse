a, b, c = map(float, input().split())

A = a**2
B = b**2
C = c**2

if (A == B + C or B == A + C or C == A + B):
    print('Yes')
else:
    print('No')