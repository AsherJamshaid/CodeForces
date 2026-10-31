size = int(input())
x = 0
for I in range(size):
    string = input()
    if "+" in string:
        x+=1
    elif "-" in string:
        x-=1
    else:
        continue
print(x)
    