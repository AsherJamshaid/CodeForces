t = int(input())
 
for x in range(t):
  n = int(input())
  arr1 = input()
  arr2 = input()
  flag = False
  for y in range(n):
    if (arr1[y] == 'G' and arr2[y] == 'B') or (arr1[y] == 'B' and arr2[y] == 'G'):
      continue
    elif arr1[y] != arr2[y]:
      flag = True
      break
  if flag == True:
    print("NO")
  else:
    print("YES")