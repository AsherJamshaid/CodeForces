t = int(input())
result = []
 
for x in range(t):
    a, b = map(int, input().split())
    
    if a == 0 and b % 2 != 0:     
        result.append("NO")
    elif (a % 2 != 0) and (b % 2 != 0):
        result.append("NO")
    elif (a % 2 == 0) and (b % 2 == 0):
        result.append("YES")
    elif (a % 2 != 0) and (b % 2 == 0):
        result.append("NO")
    elif (a % 2 == 0) and (b % 2 != 0):
        result.append("YES")
 
for x in range(t):
    print(result[x])