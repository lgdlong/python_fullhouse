n = int(input()) # Số trường hợp

arrs = [] # Tạo mảng để lưu các trường hợp

for i in range(n):
    x, y, u, v, t = map(int, input().split())
    arr = [x, y, u, v, t]
    arrs.append(arr)

print(arrs)


'''
Tony đã giành chiến thắng và nhận giải thưởng của anh Hiếu. Tony dự định mua quà về để tặng cho các bạn trong lớp của mình. Tony dự dịnh sẽ mua hai loại kẹo về để tặng các bạn. Tony mua x cái kẹo loại thứ nhất và y cái kẹo loại thứ 2.
Loại kẹo thứ nhất có giá là u đồng cái, loại thứ hai có giá v đồng một cái. Bà chủ quán cũng là người yêu thích lập trình, biết rằng Tony vừa mới đc thưởng của anh Hiếu vì học giỏi nên khuyến mãi thêm cho Tony một tùy chọn. Đó là sau khi mua, Tony có thể đổi một cái kẹo loại này lấy một cái kẹo loại kia với chi phí đổi là t đồng.

Bạn hãy lập trình giúp Tony tính số tiền ít nhất phải trả để mua kẹo nếu bạn ấy mua theo cách tối ưu nhất. Nhất định Tony phải mua đúng x cái loại 1 và y cái loại 2

INPUT FORMAT
Dòng đầu tiên là N
- các trường hợp mua kẹo mà Tony cần tính (1≤N≤20)

 dòng sau: Mỗi dòng là x,y,u,v,t
 số nguyên (1≤x,y,u,v,t≤320)
.

OUTPUT FORMAT
In ra màn hình N
dòng, mỗi dòng là số tiền ít nhất cần trả cho một trường hợp.
'''