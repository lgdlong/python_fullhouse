'''
Viết chương trình nhập vào ba số thực a,b,c
. Sau đó kiểm tra xem ba số này có tạo thành cạnh của tam giác hay không. kiểm tra xem nó thuộc loại nào trong số các loại sau:

VUONG CAN, VUONG, CAN, DEU, THUONG, KHONGPHAITAMGIAC
'''

a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("DEU")
    elif a == b or b == c or a == c:
        if round(a**2 + b**2, 5) == round(c**2, 5) or round(a**2 + c**2, 5) == round(b**2, 5) or round(b**2 + c**2, 5) == round(a**2, 5):
            print("VUONG CAN")
        else:
            print("CAN")
    elif round(a**2 + b**2, 5) == round(c**2, 5) or round(a**2 + c**2, 5) == round(b**2, 5) or round(b**2 + c**2, 5) == round(a**2, 5):
        print("VUONG")
    else:
        print("THUONG")
else:
    print("KHONGPHAITAMGIAC")


