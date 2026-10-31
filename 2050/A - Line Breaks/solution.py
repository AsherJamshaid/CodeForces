t = int(input())
result = []
 
 
for x in range(t):
    n,m = map(int,input().split())
    count = 0
    tot_length = 0
    for y in range(n):
        ch = input()
        tot_length+=len(ch)
        if tot_length  <= m:
            count+=1
    result.append(count)
    
for x in range(t):
    print(result[x])