t = int(input())
result = []
for x in range(t):
    new = ""
    string = input()
    if len(string) == 1:
        result.append("i")
    else:
    
        for y in range(len(string)-2):
            new+=string[y]
    new+="i"
    result.append(new)
    
for x in range(t):
    print(result[x])