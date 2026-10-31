t = int(input())
result = []
 
for x in range(t):
    n = int(input())
    string = input()
    count = 0
    new = []
    for y in range(n):
        if string[y] not in new:
            new.append(string[y])
            count+=2
        else:
            count+=1
    result.append(count)
    
for x in range(t):
    print(result[x])