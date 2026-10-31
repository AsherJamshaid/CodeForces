t = int(input())
 
result = []
 
for x in range(t):
    a,b,c = map(int,input().split())
    if a + b == c:
        result.append("+")
    elif a - b == c:
        result.append("-")
        
    
for x in range(t):
    print(result[x])