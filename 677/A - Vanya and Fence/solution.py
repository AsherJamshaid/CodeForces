n , h = map(int,input().split())
normal = 1
bend = 2
result = 0
heights = input().split()
for x in range(n):
 
    n1 = int(heights[x])
    if n1>h:
        result+=bend
    else:
        result+=normal
print(result)