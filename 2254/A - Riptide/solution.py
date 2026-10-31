t = int(input())
 
for x in range(t):
  arr= list(map(int,input().split()))
  arr.sort()
  ans = 0
  while( arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]):
    arr[0]+=1
    arr[2]-=1
    ans+=1
  print(ans)