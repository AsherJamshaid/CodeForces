import sys
sys.setrecursionlimit(10000)
 
 
n = int(input())
 
children = [[] for x in range(n)]
roots = []
 
for x in range(n):
    p = int(input())
 
    if p == -1:
        roots.append(x)
    else:
        children[p - 1].append(x)
 
 
def dfs(node):
    if len(children[node]) == 0:
        return 1
 
    max_child = 0
 
    for child in children[node]:
        max_child = max(max_child, dfs(child))
 
    return max_child + 1
 
 
ans= 0
 
for root in roots:
    ans = max(ans, dfs(root))
 
print(ans)