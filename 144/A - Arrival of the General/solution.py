n = int(input())
arr = list(map(int, input().split()))
 
max_val = max(arr)
min_val = min(arr)
 
max_index = arr.index(max_val)          # first max
min_index = n - 1 - arr[::-1].index(min_val)   # last min
 
swaps = max_index + (n - 1 - min_index)
 
if max_index > min_index:
    swaps -= 1
 
print(swaps)