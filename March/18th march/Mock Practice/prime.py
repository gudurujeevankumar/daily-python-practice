# 5.⁠ ⁠Check whether a number is prime.

num = int(input("Enter the number : "))
fac = 0

for i in range (1,num+1):
    if num % i == 0:
        fac += 1 

if fac == 2 :
    print("Given number is a prime number")
else:
    print("Given number is not a prime number")
