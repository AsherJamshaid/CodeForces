num ,k=map(int,input().split())
 
 
for x in range(k):
 
    last_digit = num  % 10
    if last_digit == 0 :
        num = num // 10
    else:
        num-=1
    
print(num)