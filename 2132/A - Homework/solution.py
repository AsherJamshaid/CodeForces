t = int(input())
 
result = []
 
for x in range(t):
    n = int(input())
    stra = input()
    m = int(input())
    strb = input()
    strc = input()
    
    for y in range(m):
        if strc[y] == "D":
            stra+=strb[y]
        elif strc[y] == "V":
            stra = strb[y] + stra
    result.append(stra)
for x in range(t):
    print(result[x])