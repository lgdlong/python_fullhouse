def print_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Nhập giá trị n từ người dùng
n = int(input())
print_triangle(n)
