t = int(input())
 
 
for x in range(t):
    arr = []
    a ,b = map(int,input().split())
    arr.append(min(a,b))
    arr.append(max(a,b))
    
    print(*arr)