n = int(input())
arr = list(map(int, input().split()))
 
count1 = count2 = count3 = 0
 
for num in arr:
    if num == 1:
        count1 += 1
    elif num == 2:
        count2 += 1
    else:
        count3 += 1
 
max_freq = max(count1, count2, count3)
 
print(n - max_freq)