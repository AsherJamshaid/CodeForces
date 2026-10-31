t = int(input())
for x in range(t):
    n, w = map(int, input().split())
    
    if w > n:
        print(n)
    else:
        print(n - n // w)