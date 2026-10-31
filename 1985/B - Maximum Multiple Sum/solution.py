t = int(input())
result = []
for x in range(t):
    n = int(input())
    max = 0
    for y in range(2,n+1):
        sum = 0
        count = 1
        while True:
            table = y * count
            if table<=n:
                sum+=table
                count+=1
            else:
                break
        if sum > max:
            max = sum
            value = y
    result.append(value)
for x in range(t):
    print(result[x])