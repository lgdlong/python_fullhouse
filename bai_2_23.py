'''
Cho ba số nguyên m,n,k(m<n<k và ≠0)
Kiểm tra ba số này theo thứ tự nhập vào có tạo thành một cấp số nhân hay không.

Cách làm:
So sánh thương của m, n và n, k. Nếu  2 thương bằng nhau thì là một cấp số nhân
'''

def cap_so_nhan(m, n, k):
    first_ratio = m / n
    second_ratio = n / k
    if first_ratio == second_ratio:
        print('YES')
    else:
        print('NO')

m, n, k = map(int, input().split())

cap_so_nhan(m, n, k)