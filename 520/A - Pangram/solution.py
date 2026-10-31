n = int(input())
strin = input().lower()
new = set(strin)
length = len(new)
if length == 26:
    print("YES")
else:
    print("NO")