a, b = map(int, input().split())

if (a == 0):
    print('VO NGHIEM')
elif (a == 0 and b == 0):
    print('VO SO NGHIEM')
else:
    print('PT CO NGHIEM')
    print('X = ', round(-b/a, 2))