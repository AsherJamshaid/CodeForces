import math
t = int(input())
result = []
 
for x in range(t):
    n = int(input())
    ans = n % 4
    if ans == 0:
        result.append(n//4)
    else:
        result.append(math.ceil(n/4))
for x in range(t):
    print(result[x])