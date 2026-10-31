n = int(input())
arr =list(map(int,input().split()))
arr2 =list(map(int,input().split()))
a = arr[0]
b = arr2[0]
new = arr[1::]
new2 = arr2[1::]
flag = False
for x in range(1,n+1):
    if x not in new and x not in new2:
        flag = True
        break
if flag == True:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")