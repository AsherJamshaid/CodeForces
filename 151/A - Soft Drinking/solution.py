n, k, l, c, d, p, nl, np = map(int,input().split())
 
result = int((k*l)/nl)
result2 = c * d
result3 = int(p/np)
 
print(int(min(result,result2,result3) / n))