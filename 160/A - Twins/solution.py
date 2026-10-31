n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
total = 0
coins = 0
ans = sum(arr)
 
for x in range(len(arr)):
    ans -= arr[x]
    total +=arr[x]
    coins+=1
    if total > ans:
        break
print(coins)