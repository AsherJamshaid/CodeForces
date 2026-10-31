t = int(input())
result = []
for x in range(t):
    k,x = map(int,input().split())
    
    for y in range(k):
        x*=2
    result.append(x)
for x in range(t):
    print(result[x])