import math

def devisors(n):
    arr = []
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            arr.append(i)
            if i != 1:
                arr.append(n // i)
    return arr
def is_perfect_num(n):
    if sum(devisors(n)) == n:
        print('YES')
    else:
        print('NO')
    
n = int(input())

for i in range(n):
    print(is_perfect_num(int(input())))