arr = []
t = int(input())
 
for x in range(1,10000):
  if x % 10 == 3 or x % 3 == 0 or (x % 10 == 3 and x % 3 == 0):
    continue
  arr.append(x)
for x in range(t):
  k = int(input())
  print(arr[k-1])