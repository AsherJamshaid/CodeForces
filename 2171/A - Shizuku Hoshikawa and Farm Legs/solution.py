t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    if n % 2 !=0:
        result.append(0)
    else:
        value = int(n / 4)
        result.append(value+1)
for x in range(t):
    print(result[x])