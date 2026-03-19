# 1.⁠ ⁠Check whether a number is a palindrome.

num = int(input("Enter the number : "))
lastdig = 0
revnum = 0

# we are assigning the input number to another number because the 
# input will became zero after below iteration
nu = num

# for reversing number
while num > 0:
    lastdig = num % 10
    revnum = 10 * revnum + lastdig
    num //= 10 

#for comparing the both numbers 

if nu == revnum:
    print("Palindrome")
else:
    print("Not a palindrome")

