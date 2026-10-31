t = int(input())
arr = []
for x in range(t):
    a,b,c = map(str,input().split())
    arr.append(a[0]+b[0]+c[0])
 
for x in range(t):
    print(arr[x])