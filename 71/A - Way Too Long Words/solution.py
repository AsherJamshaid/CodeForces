array_size = int(input())
ans = [""] * array_size
for x in range(array_size):
    new = ""
    string = input()
    size = len(string)
    if size > 10:
        first = string[0]
        last = string[size-1]
        new = new + first
        size2 = size - 2
        new = new + str(size2)
        new = new + last
        ans[x] = new
    else:
        ans[x] = string
print()
for x in range(len(ans)):
    print(ans[x])