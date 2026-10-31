k, n, w = map(int, input().split())
cost = 1
temp = 0
for x in range(w):
    temp += (k*(x+1))
result = temp - n
if result < 0 or result == 0:
    print("0")
else:
    print(result)