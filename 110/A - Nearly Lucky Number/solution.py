n = int(input())
temp1 =0
temp2 = 0
count = 0
while n != 0:
    temp1 = n % 10
    temp2 = n // 10
 
    if temp1 == 4 or temp1 == 7:
        count+=1
    n = temp2
 
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")