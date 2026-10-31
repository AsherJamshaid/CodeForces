t = int(input())
for x in range(t):
    result = []
    n = int(input())
    for y in range(n):
        strin = input()
        for z in range(len(strin)):
            if strin[z] == "#":
                result.append(z+1)
                break
    result.reverse()
    print(*result)