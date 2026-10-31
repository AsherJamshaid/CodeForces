n = int(input())
arr = list(map(int,input().split()))
count = 0
if n == 1:
    print(0)
else:
    arr.sort()
    max_val = max(arr)
    for x in range(n-1):
        count+=(max_val-arr[x])
    print(count)