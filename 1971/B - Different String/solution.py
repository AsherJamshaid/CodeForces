t = int(input())
arr = []
 
for x in range(t):
    string = input()
    flag = False
    
    if len(string) == 1:
        arr.append("NO")
    else:
        for y in range(len(string)):
            for z in range(y + 1, len(string)):
                if string[y] != string[z]:
                    flag = True
                    break
        
        if flag:
            arr.append("YES")
            sorted_str = "".join(sorted(string))
            
            if sorted_str == string:
                arr.append(sorted_str[::-1])
            else:
                arr.append(sorted_str)
        else:
            arr.append("NO")
 
for x in range(len(arr)):
    print(arr[x])