n,k = map(int,input().split())
 
arr = list(map(int,input().split()))
res = 0
temp = arr[k-1]
for x in range(len(arr)):
    if arr[x] == 0:
        continue
 
    elif arr[x] >= temp:
        res+=1
    
print(res)