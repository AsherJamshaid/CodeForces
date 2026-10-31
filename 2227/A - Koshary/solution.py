t = int(input())
 
for x in range(t):
    a,b = map(int,input().split())
    if (a % 2 != 0) and (b % 2 != 0):
        print("NO")
    
    elif (a % 2 == 0) and (b % 2 == 0):
        print("YES")
    elif ((a % 2 != 0 ) and (b % 2 == 0)) or ((a % 2 == 0) and (b % 2 != 0)):
        print("YES")