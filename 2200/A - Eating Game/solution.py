t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    Max = max(arr)
    print(arr.count(Max))