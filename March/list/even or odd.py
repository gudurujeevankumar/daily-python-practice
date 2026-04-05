list = list(map(eval,input().split()))

#even or odd
even = 0
odd = 0

for i in list:
    if i & 1:
        odd +=1
    else:
        even += 1
print("even : ",even)
print("odd : ",odd)
