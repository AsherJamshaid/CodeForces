cases = int(input())
ans = []
for x in range(cases):
    length = int(input())
    input_String = input()
    found = 0
    if length == 5:
        for y in range(len(input_String)):
            if input_String[y] == "T":
                found = 1 
                break
        if found == 1 and "i" in input_String and "m" in input_String and "u" in input_String and "r" in input_String:
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        ans.append("NO")
for z in range(len(ans)):
    print(ans[z])