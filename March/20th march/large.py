# 3.⁠ ⁠Find the largest element in an array.

my_list = list(map(int, input().split()))

largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)