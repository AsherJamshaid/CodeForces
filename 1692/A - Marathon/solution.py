t = int(input())
result = []
 
for x in range(t):
    count = 0
    a,b,c,d = map(int,input().split())
    if a < b:
        count+=1
    if a < c :
        count+=1
    if a < d:
        count += 1
    result.append(count)
for x in range(t):
    print(result[x])