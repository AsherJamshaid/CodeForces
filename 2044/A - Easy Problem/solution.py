t = int(input())
result =[]
 
for x in range(t):
        n = int(input())
        count = 0
        for y in range(1,n):
            for z in range(1,n):
                if y + z == n:
                    count+=1
        result.append(count)
for x in range(t):
    print(result[x])