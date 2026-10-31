t = int(input())
 
result = []
for x in range(t):
    n, s , y = map(int,input().split())
    
    arr = list(map(int,input().split()))
    total = sum(arr)
    if total > s:
        result.append("NO")
    elif total == s:
        result.append("YES")
    else:
        while True:
            total+=y
            if total > s:
                result.append("NO")
                break
            elif total == s:
                result.append("YES")
                break
for x in range(t):
    print(result[x])