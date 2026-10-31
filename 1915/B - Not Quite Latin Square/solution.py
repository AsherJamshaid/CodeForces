t = int(input())
result = []
for x in range(t):
    str1 = input()
    str2 = input()
    str3 = input()
    
    if "A" not in str1 or "A" not in str2 or "A" not in str3:
        result.append("A")
    elif "B" not in str1 or "B" not in str2 or "B" not in str3:
        result.append("B")
    elif "C" not in str1 or "C" not in str2 or "C" not in str3:
        result.append("C")
for x in range(t):
    print(result[x])