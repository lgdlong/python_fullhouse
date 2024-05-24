'''
Nhà Tèo trong khu vực sinh thái được ban quản lý cấp nhà và đào hồ cá. Hồ cá nhà bạn tèo được đào có mặt hồ là hình chữ nhật kích thước (a,b) đơn vị mét. Bố Tèo thì lại sợ rằng tèo còn nhỏ quá rơi xuống hồ thì khổ. Nên bố quyết định chỉ đưa vào hồ một lượng nước vừa đủ để lỡ Tèo rơi xuống hồ thì mức nước tối đa chỉ ngập đến cổ Tèo. Bố đã đo được chiều cao cổ Tè (tính từ mặt đất) là k (cm). Khổ nổi cái máy bơm nước nó không có chế độ chọn lượng nước mà chỉ có thể tắt sau một thời gian nào đấy.

Giả sử rằng bố đã bơm nước trong thời gian là t (giờ), công suất máy bơm là 3
(m3 / giờ). Bạn hãy giúp bố Tèo tính xem liệu với cách bơm trong t (giờ) này thì Tèo có an toàn khi rơi xuống hồ hay không. Tèo sẽ an toàn nếu mức nước cao không quá.

Bạn hãy lập trình nhập lần lượt a,b,k,t từ bàn phím. Thông báo ra màn hình YES nếu Tèo an toàn, thông báo WARNING nếu Tèo gặp nguy hiểm

a, b: Diện tích mặt hồ
k: chiều cao của Tèo
t: thời gian báo cáo
'''

a, b, k, t = map(int, input().split())



