#Dynamic list input
list = list(map(int,input("Enter list :").split()))
# list = [1,2,3,4,5,6,7,9]
ll = 0 #for storing list length

for i in list:
    ll += 1

revlist = [0]*ll
for i in range(ll):
    revlist[i] = list[ll-i-1]

print(revlist)