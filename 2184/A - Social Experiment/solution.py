t = int(input())
arr = []
 
for x in range(t):
    result = 0
    first = 0
    second = 0
    count2 = 0
    count3 = 0
    n = int(input())
    if n == 2:
        arr.append(2)
    elif n == 3 : 
        arr.append(3)
 
    elif (n>=4 and n %2 == 0):
        arr.append(0)
    elif(n>=5 and n%2 !=0):
        arr.append(1)
 
for x in range(t):
    print(arr[x])