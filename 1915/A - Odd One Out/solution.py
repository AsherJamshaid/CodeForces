t = int(input())
result = []
for x in range(t):
    a ,b , c = map(int,input().split())
    if (a != b) and (b == c):
        result.append(a)
    elif (b != a) and (a== c):
        result.append(b)
    elif (c != a) and (a== b):
        result.append(c)
        
for x in range(t):
    print(result[x])