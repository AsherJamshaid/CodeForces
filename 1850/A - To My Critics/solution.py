t = int(input())
 
result = []
 
for x in range(t):
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    if arr[0] + arr[1] >= 10:
        result.append("YES")
    else:
        result.append("NO")
for x in range(t):
    print(result[x])