import sys
input = sys.stdin.readline
 
t = int(input())
 
for x in range(t):
    n, k = map(int, input().split())
    s = input().strip()
 
    ans = 0
 
    for y in range(0, n, k):
        farm = s[y:y+k]
 
        if '0' not in farm:
            ans += 1
 
    print(ans)