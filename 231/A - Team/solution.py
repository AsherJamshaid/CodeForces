n = int(input())
ans = 0
for x in range(n):
    arr = list(map(int,input().split()))
    if sum(arr) >= 2:
        ans+=1
print(ans)