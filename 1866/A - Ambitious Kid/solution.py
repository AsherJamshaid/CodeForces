n = int(input())
arr = list(map(int,input().split()))
 
 
for x in range(len(arr)):
    if arr[x] < 0:
        arr[x] = abs(arr[x])
        
count = 0
arr.sort()
while True:
    if arr[0] == 0:
        break
    else:
        arr[0]-=1
        count+=1
        
print(count)