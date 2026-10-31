t  = int(input())
result = []
 
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = False
    for y in range(n):
        if y == n- 1:
            break
        elif (abs(arr[y] - arr[y+1])) == 5 or (abs(arr[y] - arr[y+1])) == 7:
            continue
        else:
            flag = True
            break
    if flag == True:
        result.append("NO")
    else:
        result.append("YES")
for x in range(t):
    print(result[x])