t = int(input())
 
for _ in range(t):
    n = int(input())
    
    # Check if n is a power of 2
    if n & (n - 1) == 0:
        print("NO")
    else:
        print("YES")