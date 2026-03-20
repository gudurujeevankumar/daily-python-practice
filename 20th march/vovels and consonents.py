#1.⁠ ⁠Count number of vowels and consonants in a string.


s = input("Enter the string : ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

v_count = 0
c_count = 0

for ch in s:
    if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Count of vowels in string : ", v_count)
print("Count of consonents in string : ", c_count)