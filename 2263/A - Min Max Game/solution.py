import sys
input = sys.stdin.readline
t= int(input())
 
for x in range(t):
  oneC = 0
  zeroC = 0
  n = int(input())
  arr = list(map(int,input().split()))
 
  for y in range(n):
    if arr[y] == 0:
      zeroC+=1
    else:
      oneC+=1
  if oneC >= zeroC:
    print("Bessie")
  else:
    print("Elsie")