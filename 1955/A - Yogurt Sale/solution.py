t = int(input())
 
for _ in range(t):
    n, a, b = map(int, input().split())
    
    if b < 2 * a:
        cost = (n // 2) * b + (n % 2) * a
    else:
        cost = n * a
        
    print(cost)