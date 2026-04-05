# 2.⁠ ⁠Reverse a string without using built-in functions.

s = input("Enter the string : ")
revS = ""
s_count = 0

for ch in s:
    s_count += 1

for i in range(s_count-1,0,-1):
    revS += s[i]

print(revS)