t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    p = input()
    q = input()
 
    p += "six"
 
    if sorted(p) == sorted(q + "sixsix"):
        print("YES")
    else:
        print("NO")