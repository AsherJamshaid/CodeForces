t = int(input())
 
board = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1]
]
 
ans = []
 
for _ in range(t):
    arr = [input() for _ in range(10)]
 
    total = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == "X":
                total += board[i][j]
 
    ans.append(total)
 
for x in range(len(ans)):
    print(ans[x])