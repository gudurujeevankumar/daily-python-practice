# 4.⁠ ⁠Find the factorial of a number.

# n! = n x (n-1) x (n-2) x ... x 1

num = int(input("Enter the number to find out the factorial : "))
fac = 1

for i in range(num,0,-1):
    fac *= i
print(fac)