t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    max = 0
    count = 0
    for y in range(n):
        if arr[y] == 1:
            count = 0
        elif arr[y] == 0:
            count+=1
            if count > max:
                max = count
    result.append(max)
for x in range(t):
    print(result[x])
            