q = int(input())
arr = []
for x in range(q):
    n = int(input())
    s, t = map(str,input().split())
    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))
    if sorted_s == sorted_t:
        arr.append("YES")
    else:
        arr.append("NO")
 
for x in range(q):
    print(arr[x])