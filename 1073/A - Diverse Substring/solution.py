length = int(input())
string = input()
 
found = False
for i in range(length - 1):
    if string[i] != string[i+1]:
        print("YES")
        print(string[i] + string[i+1])
        found = True
        break
 
if not found:
    print("NO")