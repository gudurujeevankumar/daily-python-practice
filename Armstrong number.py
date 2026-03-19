n = int(input("Enter the number : "))
last = 0
count = 0

num = n 

while n > 0:
    count += 1
    n //= 10

for i in range(count):
    last = num % 10
    print(last)
    n //= 10
