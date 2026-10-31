n = int(input())
integer = input().split()
one_count = 0
zero_count = 0
for x in range(n):
 
    n1 = int(integer[x])
    if n1 == 1:
        one_count+=1
    else:
        zero_count+=1
 
if one_count >=1:
    print("HARD")
elif one_count == 0 and zero_count == n:
    print("EASY")