'''
Cho ba số nguyên m,n,k(m<n<k).
Nếu ba số này lập thành một dãy cấp số cộng thì thì tính tổng các số này còn không thông báo không phải là cấp số cộng
'''

def cap_so_cong(m, n, k):
    if (m + k) / 2 == n:
        print(sum([m, n, k]))
    else:
        print(-1)
    

m, n, k = map(int, input().split())

cap_so_cong(m, n, k)