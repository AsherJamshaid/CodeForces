t = int(input())
result = []
for x in range(t):
    string = input()
    found = False
    
    for y in range(len(string)):
        if y == len(string)-1:
            break
        elif string[y] == string[y+1]:
            found = True
            break
    if found == True:
        result.append("1")
    else:
        result.append(len(string))
        
for x in range(t):
    print(result[x])