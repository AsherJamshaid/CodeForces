t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input().strip()
    count = 0
 
    for i in range(n):
        # copy string
        temp = list(s)
 
        # flip ith character
        if temp[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
 
        # count 1s in this row
        count += temp.count('1')
 
    print(count)