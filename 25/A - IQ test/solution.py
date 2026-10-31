n = int(input())
arr = list(map(int,input().split()))
odd = []
even = []
for x in range(len(arr)):
    if arr[x] % 2 == 0:
        even.append(x+1)
    else:
        odd.append(x+1)
if len(odd) == 1:
    print(odd[0])
elif len(even) == 1:
    print(even[0])