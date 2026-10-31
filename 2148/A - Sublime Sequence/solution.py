t = int(input())
result = []
for x in range(t):
    y,n = map(int,input().split())
    sum = 0
    for z in range(1,n+1):
        if z % 2 == 0:
            sum-=y
        else:
            sum+=y
    result.append(sum)
for x in range(t):
    print(result[x])