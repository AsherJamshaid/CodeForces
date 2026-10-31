t = int(input())
 
for x in range(t):
  diff = 0
  a,b = map(int,input().split())
  if a == b:
    print(0)
    continue
  diff = abs(a - b) % 10
  if diff == 0:
    print(abs(a-b)//10)
  else:
    
    print((abs(a-b)//10) + 1)