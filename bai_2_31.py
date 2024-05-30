n = int(input())

for i in range(1, n+1):
    count = i
    dau_cach = n - i
    for j in range(dau_cach): # dau cach
        print(' ', end='')
    for g in range(1, i+1): # nua truoc tam giac
        print(g, end='')
    while(count != 1):
        print(count-1, end='')
        count -= 1
    print()
    
'''
....1
...121
..12321
.1234321
123454321
'''