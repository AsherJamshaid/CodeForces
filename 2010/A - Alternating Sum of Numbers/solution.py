t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    even_sum = 0
    odd_sum = 0
    ans = 0
    for y in range(n):
        if y % 2 == 0:
            even_sum+=arr[y]
        else:
            odd_sum+=arr[y]
    ans = even_sum - odd_sum
    result.append(ans)
for x in range(t):
    print(result[x])