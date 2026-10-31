t = int(input())
result = []
pre = "ABCDEFG"
 
for x in range(t):
    n , m = map(int,input().split())
    strin = input()
    new = set(strin)
    Acount = 0
    Bcount = 0
    Ccount = 0
    Dcount = 0
    Ecount = 0
    Fcount = 0
    Gcount = 0
    count = 0
    Acount = strin.count("A")
    if Acount < (m):
        count+= m - Acount
        
    Bcount = strin.count("B")
    if Bcount < (m):
        count+= m - Bcount
    Ccount = strin.count("C")
    if Ccount < (m):
        count+= m - Ccount
    Dcount = strin.count("D")
    if Dcount < (m):
        count+= m - Dcount
    Ecount = strin.count("E")
    if Ecount < (m):
        count+= m - Ecount
    Fcount = strin.count("F")
    if Fcount < (m):
        count+= m - Fcount
    Gcount = strin.count("G")
    if Gcount < (m):
        count+= m - Gcount
    result.append(count)
for x in range(t):
    print(result[x])