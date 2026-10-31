t = int(input())
result = []
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    zero_count= 0
    neg_count = 0
    op = 0
    
    zero_count = arr.count(0)
    neg_count = arr.count(-1)
    op+=zero_count
    if neg_count % 2 != 0:
        op+=2
    
    result.append(op)
for x in range(t):
    print(result[x])