str1 = input().lower()
str2 = input().lower()
count = 0
found = 0
size = len(str1)
for x in range(size):
    if str1[x] == str2[x]:
        count = count + 1
    elif str1[x] < str2[x]:
        found = 1
        break
    else:
        break
if count == len(str1):
    print("0")
elif found == 1:
    print("-1")
else:
    print("1")