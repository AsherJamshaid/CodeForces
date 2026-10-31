t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if 67 in arr:
        result.append("YES")
    else:
        result.append("NO")
        
for x in range(t):
    print(result[x])