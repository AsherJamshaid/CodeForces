t = int(input())
result  = []
for x in range(t):
    value = list(input())
    value.sort()
    result.append(value[0])
for x in range(t):
    print(result[x])