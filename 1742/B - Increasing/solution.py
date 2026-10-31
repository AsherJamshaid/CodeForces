t = int(input())
 
for x in range(t):
  flag = False
  n = int(input())
  arr = list(map(int,input().split()))
  arr.sort()
  if n == 1:
    print("YES")
    continue
  
  for y in range(n-1):
    if arr[y] == arr[y+1]:
      flag = True
      break
  if flag == True:
    print("NO")
  else:
    print("YES")