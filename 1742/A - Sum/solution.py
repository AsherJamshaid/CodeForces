t = int(input())
 
result = []
for x in range(t):
    a, b, c = map(int,input().split())
    if (a+b == c) or (a+c == b) or (b + c == a):
        result.append("YES")
    else:
        result.append("NO")
 
for x in range(t):
    print(result[x])