
# 2.⁠ ⁠Check whether a string is a palindrome without using any inbuilt funtions

s = input("Enter the string : ")
revS = ""
count = 0

for char in s:
    count += 1


for i in range (count,0,-1):
    revS += s[i-1]

if s == revS:
    print("Given string : " + s)
    print("Reversed string : " + revS)
    print("So, Given string is a palindrom")
else:
    print("Given string : " + s)
    print("Reversed string : " + revS)
    print("So, Given string is not a palindrom")


