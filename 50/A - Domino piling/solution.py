import math
 
n, m = map(int, input().split())
ans = n * m
if ans % 2 != 0:
    print(math.ceil(ans/2) - 1)
else:
    print(math.ceil(ans/2))