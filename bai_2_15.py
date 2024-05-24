'''
Chi nhánh điện lực Hà Nội đưa ra hai mức tính tiền điện như sau:
Dưới 200 Kwh mức giá 1500 đ/kwh
Từ 200 kwh trở lên mức giá là 3000 đ/kwh
Hãy giúp bạn tính tiền điện của nhà bạn Hiếu biết rằng tháng vừa rồi nhà bạn Hiếu tiêu thụ hết N (kwh).
'''

n = int(input()) # kWh

if (n < 200):
    print(n * 1500)
else:
    # print(200 * 1500 + (n - 200) * 3000)
    print(n * 3000)