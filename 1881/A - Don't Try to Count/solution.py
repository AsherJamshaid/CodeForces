t = int(input())
 
result = []
for x in range(t):
    n,m = map(int,input().split())
    str1 = input()
    str2 = input()
    count = 0
    while True:
        if str2 in str1:
            result.append(count)
            break
        elif len(str1) > 8 * len(str2):
            result.append(-1)
            break
        str1+=str1
        count+=1
for x in range(t):
    print(result[x])