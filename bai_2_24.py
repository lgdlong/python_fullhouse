'''
Lập trình nhập vào từ bàn phím ba số nguyên m,n,k
Tính và thông báo ra màn hình bình phương của số âm và lập phương của số dương.
'''

m, n, k = map(int, input().split())

arr = [m, n, k]

for i in arr:
    if i == 0:
        print(i, end=' ')
    elif i < 0:
        print(i**2, end=' ')
    else:
        print(i**3, end=' ')

