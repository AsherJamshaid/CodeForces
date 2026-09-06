n = int(input())
m_count = 0
c_count = 0
for x in range(n):
  m , c = map(int,input().split())
  if m > c:
    m_count+=1
  elif c > m:
    c_count+=1
  else:
    continue
if m_count > c_count:
  print("Mishka")
elif m_count < c_count:
  print("Chris")
else:
  print("Friendship is magic!^^")