# 4.⁠ ⁠Find the second largest element in an array.


my_list = list(map(int,input().split()))

f_large = float('-inf')
s_large = float('-inf')

for i in my_list:

    if i > f_large:
        s_large = f_large
        f_large = i

    elif i > s_large and i != f_large:
        s_large = i

print(s_large)
