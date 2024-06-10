'''
Cấp số cộng

Số hạng đầu tiên là a
Công sai (khoảng cách giữa hai số liên tiếp) là d
Số hạng cuối cùng là l
Số lượng các số hạng trong dãy là n


S = n * (2 * a + (n - 1) * d) / 2

1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61 64 67 70 73 76 79 82 85 88 91 94 97 100
'''

n, k = map(int, input().split())

sum = n * (2 * 1 + (n - 1) * 3) / 2

print(sum)