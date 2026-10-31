t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    count = 0
    temp = []
 
    for y in range(1, 21):
        temp.append(y)
        count += 1
        if count == n:  
            break
 
    result.append(temp)   
 
for row in result:
    print(*row)