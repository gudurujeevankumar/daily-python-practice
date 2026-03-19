# 3.⁠ ⁠Print the Fibonacci series up to N terms.

# 0 1 1 2 3 5 8 13 21
n = int(input("Enter the number of fibonacci terms to print : "))

a = 0 
b = 1
temp = 0

for i in range (n):
    print (a,end=" ")
    temp = a + b
    a = b
    b = temp

    # simple version (without using third variable)
    #  a , b = b , a+b