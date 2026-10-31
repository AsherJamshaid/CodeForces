n = int(input())
 
 
arr = list(map(int,input().split()))
sum = 0
for x in range(n):
    sum+=arr[x]
 
print(float(sum/n))