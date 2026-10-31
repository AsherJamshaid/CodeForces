t = int(input())
result = []
for x in range(t):
    string = input()
    Acount = 0 
    Bcount = 0
    for y in range(len(string)):
        if string[y] == "A":
            Acount+=1
        else:
            Bcount+=1
    if Acount > Bcount:
        result.append("A")
    else:
        result.append("B")
for x in range(t):
    print(result[x])