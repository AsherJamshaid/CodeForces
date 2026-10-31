row = 0
col = 0
for x in range(5):
    arr = list(map(int, input().split()))
    for y in range(5):
        if arr[y] == 1:
            row = x + 1
            col = y + 1
 
res = abs(row-3) + abs(col-3)
print(res)