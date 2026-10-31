n = int(input())
hashing = {}
arr = []
for x in range(n):
    temp = input()
    arr.append(temp)
for x in range(len(arr)):
    if arr[x] in hashing:
        hashing[arr[x]]+=1
    else:
        hashing[arr[x]]=1
print(max(hashing, key=hashing.get))