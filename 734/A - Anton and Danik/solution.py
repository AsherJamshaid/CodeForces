n = int(input())
 
string = input()
 
A_Count = 0
D_Count = 0
 
for x in range(n):
    if string[x] == "A":
        A_Count+=1
    elif string[x] == "D":
        D_Count+=1
    
if A_Count > D_Count:
 
    print("Anton")
elif D_Count > A_Count:
    print("Danik")
else:
    print("Friendship")