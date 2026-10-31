t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    max = 0
    index = 0
    for y in range(n):
        a,b = map(int,input().split())
        if a > 10:
            continue
        else:
            if b > max and a <= 10:
                max = b
                index = y+1
    result.append(index)
 
for x in range(t):
    print(result[x])