n = int(input())
current = 0
max = 0 
for x in range(n):
    a,b = map(int,input().split())
    current-=a
    current+=b
    if current >= max:
        max = current
print(max)