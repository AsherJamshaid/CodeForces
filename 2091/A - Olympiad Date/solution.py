# cook your dish here
 
t = int(input())
result = []
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count1 = 0
    count2 = 0
    count3 = 0
    count0 = 0
    count5 = 0
    count = 0
    flag = False
    for y in range(len(arr)):
        
        count+=1
        if arr[y] == 0:
            count0+=1
        elif arr[y] == 1:
            count1+=1
        elif arr[y] == 2:
            count2+=1
        elif arr[y] == 3:
            count3+=1
        elif arr[y] == 5:
            count5+=1
        if count0 >= 3 and count1 >= 1 and count2 >= 2 and count3 >= 1 and count5 >= 1:
            flag = True
            break
        
    if flag == False:
        result.append(0)
    else:
        result.append(count)
for x in range(t):
    print(result[x])