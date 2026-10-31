import math
 
n, m, a = map(int, input().split())
count = 0
 
first = math.ceil(n/a)
 
 
second = math.ceil(m / a)
 
 
print(first * second)