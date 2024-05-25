'''
Bạn Hiếu mất trật tự trong giờ học thể dục nên bị thầy giáo phạt.
Hình phạt của thầy như sau:
    bạn Hiếu đứng nghiêm,
    khi thầy hô "trái" thì Hiếu bước sang trái một mét,
    thầy hô "phải" thì Hiếu bước sang phải một mét.
Hỏi sau n lần thầy hô như vậy thì bạn Hiếu cách xa vị trí ban đầu bao nhiêu mét?

INPUT FORMAT
Dòng thứ nhất là số n (1≤n≤1000).
N dòng tiếp theo gồm số 1 hoặc 2, mỗi số trên 1 dòng.
Nếu là số 1 thì thầy giáo hô "trái", nếu là số 2 thì thầy giáo hô "phải".

OUTPUT FORMAT
Là khoảng cách của Hiếu sau n lần hô so với vị trí ban đầu.
'''

n = int(input())

work = []
for i in range(n):
    work.append(int(input()))

pos = 0

for i in work:
    if i == 1:
        pos -= 1
    else:
        pos += 1

print(abs(pos))