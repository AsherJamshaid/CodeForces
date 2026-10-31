n = int(input())
 
prev = input().strip()
groups = 1  
 
for x in range(n - 1):
    curr = input().strip()
    if curr != prev:
        groups += 1
    prev = curr
 
print(groups)