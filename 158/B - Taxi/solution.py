t = int(input())
arr = list(map(int, input().split()))
 
count = [0] * 5
for x in arr:
    count[x] += 1
 
taxis = count[4]          
taxis += count[3]         
count[1] -= min(count[1], count[3])  
 
taxis += count[2] // 2    
if count[2] % 2 == 1:    
    taxis += 1
    count[1] -= min(count[1], 2) 
 
taxis += (count[1] + 3) // 4 
print(taxis)