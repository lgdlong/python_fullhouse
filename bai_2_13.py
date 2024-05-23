'''
Có một trang trại Thỏ. Một hôm anh ấy tổ chức giải đua thỏ.

Con thỏ đầu tiên bắt đầu tại vị trí x1 và di chuyển v1 mét trên mỗi lần nhảy.

Con thỏ thứ hai bắt đầu tại vị trí x2 và di chuyển v2 mét trên mỗi lần nhảy.

Liệu hai con thỏ này có gặp nhau tại một điểm trong quá trình nhảy hay không.
Nếu có thể, trả lại YES, nếu không thì trả lại NO.
'''

x1, v1, x2, v2 = map(int, input().split())

if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2): # Không gặp nhau ngay từ ban đầu vì một trong 2 con chạy nhanh hơn và chạy trước
    print('NO')
else:
    if (x1 - x2) % (v2 - v1) == 0:
        # Khoảng cách ban đầu giữa hai thỏ có thể chia hết cho chênh lệch về tốc độ của chúng
        # Khi đó, cả hai thỏ sẽ đến cùng một điểm vào một lần nhảy nào đó sau khi khởi đầu.
        print('YES')
    else:
        print('NO')