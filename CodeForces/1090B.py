import sys
input = sys.stdin.readline

t = int(input())

for x in range(t):
    arr = list(map(int,input().split()))
    arr.sort()
    temp = 0
    for y in range(len(arr)-1):
        temp+=(arr[y] * -1)
    temp+=arr[6]
    print(temp)