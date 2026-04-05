# Remove duplicates from string

my_string = input("Enter the string : ")
seen = ""

for char in my_string:
    if char not in seen:
        seen = seen + char

print(seen)