t = int(input())
 
result = []
 
for x in range(t):
    arr = list(map(int,input().split()))
    arr.sort()
    result.append(arr[1])
for x in range(t):
    print(result[x])