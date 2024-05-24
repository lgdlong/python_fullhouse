'''
Viết chương trình giải phương trình bậc hai: ax2+bx+c=0
với a,b,c là các hệ số nguyên nhập vào từ bàn phím.

Kết quả thông báo theo yêu cầu, nghiệm làm tròn hai chữ số thập phân.
'''

import math

a, b, c = map(int, input().split())


if (a == 0): # PT bx+c=0
    print("X =", round(-c/b, 2))
else: # PT ax^2+bx+c=0
    delta = b**2 - 4*a*c
   
    if delta < 0:
        print("VO NGHIEM")
    elif delta == 0:
        print("PT CO NGHIEM KEP")
        print("X =", round(-b/(2*a), 2))
    else:
        print("PT CO 2 NGHIEM")
        print("X1 =", round((-b + math.sqrt(delta))/(2*a), 2))
        print("X2 =", round((-b - math.sqrt(delta))/(2*a), 2))