import math
a,b = map(int,input().split())
if a < b:
    first = a
    temp = b - a
elif a > b:
    first = b
    temp = a - b
else:
    first = a
    temp = 0
second = math.floor(temp / 2)
print(first,end=" ")
print(second)