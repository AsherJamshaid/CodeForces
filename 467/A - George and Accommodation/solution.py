rooms = int(input())
count = 0
difference = 0
 
for x in range(rooms):
    p, q = map(int , input().split())
    if p == q:
        continue
    elif (q-p) >= 2:
        count+=1
print(count)