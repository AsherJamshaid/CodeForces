arr = list(map(str,input()))
arr2 = list(map(str,input()))
result = []
 
for x in range(len(arr)):
    if arr[x] != arr2[x]:
        result.append("1")
    else:
        result.append("0")
string = ""
for x in range(len(arr)):
    string+=result[x]
 
print(string)