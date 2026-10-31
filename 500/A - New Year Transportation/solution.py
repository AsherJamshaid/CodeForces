n,t = map(int,input().split())
arr=list(map(int,input().split()))
 
curr=1
while curr<=len(arr):
    
    curr+=arr[curr-1]
    if curr==t:
        print("YES")
        break
    elif curr>t:
        print("NO")
        break