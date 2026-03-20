# 5.⁠ ⁠Calculate the sum of digits of a number.


n = int(input("Enter number : "))

sum_of_dig = 0

while n > 0:

    last = n % 10
    sum_of_dig += last
    n //= 10

print(sum_of_dig)