n, k = map(int,input().split())
arr = []
for x in range(n):
    f, t = map(int,input().split())
 
    if t > k:
        arr.append(f-(t-k))
    else:
        arr.append(f)
max = arr[0]
for x in range(len(arr)):
    if arr[x] > max:
        max = arr[x]
print(max)
    