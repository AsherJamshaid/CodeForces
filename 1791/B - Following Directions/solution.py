t = int(input())
 
result = []
x2 = 1
y2 = 1
for x in range(t):
    n = int(input())
    string = input()
    x1 = 0
    y1 = 0
    flag = False
    
    for y in range(len(string)):
        if string[y] == "U":
            y1+=1
        elif string[y] == "D":
            y1-=1
        elif string[y] == "L":
            x1-=1
        elif string[y] == "R":
            x1+=1
        if x1 == x2 and y1 == y2:
            flag = True
            break
    if flag == True:
        result.append("YES")
    else:
        result.append("NO")
 
for x in range(t):
    print(result[x])