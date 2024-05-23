'''
Mam : a
Bao : b
Chuot : c
'''

a, b, c = map(int, input().split())

mam_to_chuot = abs(a - c)
bao_to_chuot = abs(b - c)

if mam_to_chuot < bao_to_chuot:
    print('MAM')
elif bao_to_chuot < mam_to_chuot:
    print('BAO')
else:
    print('CHUOT')