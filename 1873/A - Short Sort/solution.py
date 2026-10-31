t = int(input())
result = []
for x in range(t):
    string = input()
    if string == "abc" or string == "acb" or string == "bac" or string == "cba":
        result.append("YES")
    else:
        result.append("NO")
 
for x in range(t):
    print(result[x])