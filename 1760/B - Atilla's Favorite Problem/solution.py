t = int(input())
constr = "abcdefghijklmnopqrstuvwxyz"
result = []
 
for x in range(t):
    n = int(input())
    string = input()
    max = 0
    for y in range(len(string)):
        
        for z in range(len(constr)):
            if string[y] == constr[z]:
                if z+1 > max:
                    max = z+1
    result.append(max)
for x in range(t):
    print(result[x])