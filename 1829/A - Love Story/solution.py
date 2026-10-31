t = int(input())
orig = "codeforces"
result = []
for x in range(t):
    string = input()
    count = 0
    for y in range(10):
        if string[y] != orig[y]:
            count+=1
    result.append(count)
    
for x in range(t):
    print(result[x])