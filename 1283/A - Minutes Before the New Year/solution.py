t = int(input())
result = []
for x in range(t):
    total = 0
    a,b = map(int,input().split())
    
    if a == 23 and b == 0:
        total = 1 * 60
    elif a == 23 and b!= 0:
        total = 60 - b
    else:
        total = ((23-a)*60) + (60-b)
    result.append(total)
    
for x in range(t):
    print(result[x])