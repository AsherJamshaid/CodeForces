t = int(input())
 
result = []
 
for x in range(t):
    ch = input()
    if ch in "codeforces":
        result.append("YES")
    else:
        result.append("NO")
 
 
for x in range(t):
    print(result[x])