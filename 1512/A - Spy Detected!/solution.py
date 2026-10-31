t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Count occurrences
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Find the unique number
    for num in count:
        if count[num] == 1:
            unique = num
            break
    
    # Find its index
    for i in range(n):
        if arr[i] == unique:
            print(i + 1)  # 1-based index
            break