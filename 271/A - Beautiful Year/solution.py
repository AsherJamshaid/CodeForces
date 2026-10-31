n = int(input())
 
found = False
temp = n
first=0
second=0
third=0
fourth=0
 
 
 
 
while found == False:
    temp+=1
    first = (temp%10)
    second = int((temp%100) / 10)
    third = int((temp%1000) / 100)
    fourth = int((temp%10000) / 1000)
    if temp > n:
        if first != second and first != third and first != fourth and second != first and second != third and second != fourth and third != first and third != second and third != fourth and fourth != first and fourth != second and fourth != third:
            found = True
    
print(temp)