t = int(input())
arr = []
for x in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  if arr.count(0) < 2:
    print("-1")
  elif arr.count(1) == 0:
    print("0")
  elif (arr[0] == 0 and arr[n-1] == 1) or (arr[0] == 1 and arr[n-1] == 0):
    print("1")
  elif arr[0] == 0 and arr[n-1] == 0:
    print("0")
  else:
    print("2")